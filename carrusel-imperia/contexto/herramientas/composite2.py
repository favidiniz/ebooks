import cv2, numpy as np, json, os
B='/home/user/ebooks/carrusel-imperia/assets/navidad/'; OUT=B+'fixed'; F='fix'
def src(n):
    for p in [B+'tex/'+n+'.png',B+'orig/'+n+'.png',B+'orig/'+n+'.jpg']:
        if os.path.exists(p): return p
os.makedirs(OUT,exist_ok=True)
q=json.load(open(F+'/quads2.json'))
REAL={'P':cv2.imread(F+'/real-premium-crop.png').astype(np.float32),'S':cv2.imread(F+'/real-sanremo.png').astype(np.float32)}
KIND={'m-p':'P','m-s2':'P','m-s3':'P','m-s4':'P','c-p':'P','c-s2':'P','c-s3':'P','c-s4':'P','v-p':'S','v-s3':'S','s-p':'S','s-s2':'S','s-s3':'S'}
rng=np.random.default_rng(3)
def stats_dark_gold(img,mask):
    px=img[mask>0].reshape(-1,3); lum=px.mean(1)
    dark=np.median(px[lum<np.percentile(lum,40)],0)
    hsv=cv2.cvtColor(np.clip(img,0,255).astype(np.uint8),cv2.COLOR_BGR2HSV)[mask>0]
    g=(hsv[:,1]>90)&(hsv[:,2]>110)
    gold=px[g].mean(0) if g.sum()>30 else np.percentile(px,97,axis=0)
    return dark,gold
tiles=[]
for n,kind in KIND.items():
    im=cv2.imread(src(n)).astype(np.float32); Hh,Ww=im.shape[:2]
    Q=np.array(q[n],dtype=np.float32)
    real=REAL[kind]; rh,rw=real.shape[:2]; Ar=rw/rh
    wt=(np.linalg.norm(Q[1]-Q[0])+np.linalg.norm(Q[2]-Q[3]))/2; ht=(np.linalg.norm(Q[3]-Q[0])+np.linalg.norm(Q[2]-Q[1]))/2; At=wt/ht
    Ae=float(np.clip(At,Ar/1.12,Ar*1.12)); m=0.035
    if At>Ae: k=At/Ae; u0,u1=-m,1+m; v0,v1=-(k-1)/2-m*k,1+(k-1)/2+m*k
    else: k=Ae/At; u0,u1=-(k-1)/2-m*k,1+(k-1)/2+m*k; v0,v1=-m,1+m
    Hq=cv2.getPerspectiveTransform(np.float32([[0,0],[1,0],[1,1],[0,1]]),Q)
    rect=np.float32([[u0,v0],[u1,v0],[u1,v1],[u0,v1]]).reshape(-1,1,2)
    dst=cv2.perspectiveTransform(rect,Hq).reshape(-1,2)
    # pre-resize to about target size
    tw=int(np.linalg.norm(dst[1]-dst[0])*1.5); th=int(tw/ Ar * ( (v1-v0)/(u1-u0) * At / Ar ) ) if False else int(np.linalg.norm(dst[3]-dst[0])*1.5)
    rs=cv2.resize(real,(max(tw,8),max(th,8)),interpolation=cv2.INTER_AREA)
    Hm=cv2.getPerspectiveTransform(np.float32([[0,0],[rs.shape[1],0],[rs.shape[1],rs.shape[0]],[0,rs.shape[0]]]),dst)
    warped=cv2.warpPerspective(rs,Hm,(Ww,Hh),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REPLICATE)
    mask=cv2.warpPerspective(np.full(rs.shape[:2],255,np.uint8),Hm,(Ww,Hh),flags=cv2.INTER_LINEAR)
    fq=np.zeros((Hh,Ww),np.uint8); cv2.fillPoly(fq,[Q.astype(np.int32)],255)
    # color mapping
    core=cv2.erode(mask,np.ones((7,7),np.uint8)); rp=warped[core>0].reshape(-1,3); fp=im[fq>0].reshape(-1,3)
    if kind=='P':
        dr=np.percentile(rp,30,axis=0); df=np.percentile(fp,30,axis=0)
        def gold(px):
            hsv=cv2.cvtColor(np.clip(px,0,255).astype(np.uint8).reshape(-1,1,3),cv2.COLOR_BGR2HSV).reshape(-1,3)
            sel=(hsv[:,1]>70)&(hsv[:,0]>8)&(hsv[:,0]<35)
            v=hsv[:,2]; sel2=sel&(v>=np.percentile(v[sel],85))
            return px[sel2].mean(0)
        gr=gold(rp); gf=gold(fp)
        slope=np.clip((gf-df)/np.maximum(gr-dr,1),0.6,2.2)
        warped=(warped-dr)*slope+df
    else:
        wr=np.percentile(rp,85,axis=0); dr=np.percentile(rp,4,axis=0)
        if n.startswith('s-') or n.startswith('v-'):
            wf=np.percentile(fp,85,axis=0)*0.97
        else:
            x0,y0=Q.min(0).astype(int); x1,y1=Q.max(0).astype(int)
            reg=im[max(0,y0-260):y1+20,max(0,x0-150):min(Ww,x1+150)].reshape(-1,3)
            wf=np.percentile(reg,96,axis=0)*0.86
        df=wf*0.14
        warped=(warped-dr)*(wf-df)/np.maximum(wr-dr,1)+df
    # match softness + grain
    if kind=='S': warped=cv2.GaussianBlur(warped,(0,0),0.5)
    warped+=rng.normal(0,1.6,warped.shape).astype(np.float32)
    a=cv2.GaussianBlur(cv2.erode(mask,np.ones((3,3),np.uint8)),(0,0),1.0).astype(np.float32)[...,None]/255
    # soft contact shadow just outside the label
    sh=cv2.GaussianBlur(cv2.dilate(mask,np.ones((5,5),np.uint8)),(0,0),3).astype(np.float32)[...,None]/255
    base=im*(1-0.22*sh*(1-a))
    out=np.clip(base*(1-a)+warped*a,0,255).astype(np.uint8)
    cv2.imwrite(f'{OUT}/{n}.png',out)
    x0,y0=dst.min(0).astype(int)-50; x1,y1=dst.max(0).astype(int)+50; x0=max(0,x0);y0=max(0,y0)
    b=im[y0:y1,x0:x1].astype(np.uint8); c=out[y0:y1,x0:x1]
    t=np.hstack([b,c]); t=cv2.resize(t,(720,int(720*t.shape[0]/t.shape[1]))); cv2.putText(t,n,(5,18),0,.55,(0,0,255),2); tiles.append(t)
hmax=max(t.shape[0] for t in tiles); tiles=[cv2.copyMakeBorder(t,0,hmax-t.shape[0]+4,0,4,cv2.BORDER_CONSTANT,value=(60,60,60)) for t in tiles]
rows=[np.hstack(tiles[i:i+2]+[np.zeros_like(tiles[0])]*(2-len(tiles[i:i+2]))) for i in range(0,len(tiles),2)]
cv2.imwrite(F+'/ba.jpg',np.vstack(rows))
