import cv2, numpy as np, sys, json
O='/home/user/ebooks/carrusel-imperia/assets/navidad/orig/'; T='/home/user/ebooks/carrusel-imperia/assets/navidad/tex/'
F='/tmp/claude-0/-home-user-ebooks/578aafb8-e622-52a6-8fca-47556ff481b3/scratchpad/fix/'
import os; os.makedirs(T,exist_ok=True)
ref=cv2.imread(F+'r7166.jpg').astype(np.float32)
strip=cv2.cvtColor(ref[1114:1426,560:1240],cv2.COLOR_BGR2GRAY)
# period via autocorrelation of column means of high-pass
c=strip.mean(0); c=c-c.mean()
ac=np.correlate(c,c,'full')[len(c)-1:]; ac/=ac[0]
p=int(np.argmax(ac[170:330])+170); print('period',p)
k=max(1,(strip.shape[1])//p); tile=strip[:,:k*p]
th,tw=tile.shape
def lowpass_masked(img,mask,s):
    m=mask.astype(np.float32)
    num=cv2.GaussianBlur(img*m[...,None] if img.ndim==3 else img*m,(0,0),s)
    den=cv2.GaussianBlur(m,(0,0),s)+1e-4
    return num/(den[...,None] if img.ndim==3 else den)
LINES={
'm-p.png':{'top':((0,1250),(1122,1230)),'h':168},
'm-s2.png':{'top':((0,1248),(1122,1228)),'h':168},
'm-s3.png':{'sat':120,'vmin':25,'vmax':185,'top':((0,1178),(1122,1226)),'h':232},
'm-s4.png':{'sat':120,'vmin':25,'vmax':185,'top':((130,1216),(1122,1166)),'h':156,'x':(128,1122)},
'c-p.png':{'sat':100,'vmin':30,'vmax':175,'top':((0,1205),(1122,1137)),'h':118,'ex':[[(555,1000),(805,1000),(805,1280),(555,1300)]]},
'c-s2.png':{'sat':100,'vmin':30,'vmax':175,'top':((0,1176),(740,1110)),'h':172,'x':(0,738)},
'c-s3.png':{'sat':100,'vmin':30,'vmax':175,'top':((0,1292),(1122,1094)),'h':250},
'c-s4.png':{'sat':100,'vmin':30,'vmax':175,'top':((0,1226),(600,1150)),'h':205,'x':(0,600)},
}
names=sys.argv[1:]
dbg=[]
for n in names:
    im=cv2.imread(O+n).astype(np.float32); H,W=im.shape[:2]
    hsv=cv2.cvtColor(cv2.medianBlur(im.astype(np.uint8),11),cv2.COLOR_BGR2HSV)
    v=hsv[...,2].astype(np.float32); sat=hsv[...,1]
    L=LINES[n]; (tx0,ty0),(tx1,ty1)=L['top']; bh=L['h']
    a=np.polyfit([tx0,tx1],[ty0,ty1],1); b=a.copy(); b[1]+=bh
    x0,x1=L.get('x',(0,W))
    xs=np.arange(x0,x1,4); hmean=bh
    m=((sat<(L.get('sat',62)))&(v>L.get('vmin',70))&(v<L.get('vmax',200))).astype(np.uint8)
    for poly in L.get('ex',[]): cv2.fillPoly(m,[np.int32(poly)],0)
    # build texture across width: scale tile height to hmean
    sc=hmean/th; reps=int(np.ceil((x1-x0)/(tw*sc)))+1
    big=np.tile(tile,(1,reps)); bw=big.shape[1]
    src=np.float32([[0,0],[bw,0],[bw,th],[0,th]])
    X1=x0+bw*sc
    dst=np.float32([[x0,np.polyval(a,x0)],[X1,np.polyval(a,X1)],[X1,np.polyval(b,X1)],[x0,np.polyval(b,x0)]])
    Hm=cv2.getPerspectiveTransform(src,dst)
    tex=cv2.warpPerspective(big,Hm,(W,H),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REFLECT)
    s=max(6,hmean/4)
    texlp=cv2.GaussianBlur(tex,(0,0),s)+1
    tex=np.clip(tex,1,255); ratio=np.power(tex/texlp,0.8)
    # region: inside band polygon AND mask (excludes occluders/label)
    band=np.zeros((H,W),np.uint8); cv2.fillPoly(band,[np.int32([[x0,np.polyval(a,x0)+7],[x1,np.polyval(a,x1)+7],[x1,np.polyval(b,x1)-3],[x0,np.polyval(b,x0)-3]])],1)
    reg=(band&m).astype(np.float32)
    reg=cv2.erode(reg,np.ones((5,5),np.uint8)); print(n,'cover',round(reg.sum()/max(band.sum(),1),2))
    lp=lowpass_masked(im,reg,s*1.6)
    new=lp*ratio[...,None]
    # match contrast of original high freq a bit: blend
    alpha=cv2.GaussianBlur(reg,(0,0),2.5)[...,None]*0.88
    out=im*(1-alpha)+new*alpha
    ext='.png'
    cv2.imwrite(T+n.rsplit('.',1)[0]+'.png',np.clip(out,0,255).astype(np.uint8))
    y0=int(np.polyval(a,W/2))-60; y1=min(H,int(np.polyval(b,W/2))+40)
    pair=np.hstack([im[y0:y1],out[y0:y1]]).astype(np.uint8)
    pair=cv2.resize(pair,(1400,int(1400*pair.shape[0]/pair.shape[1])))
    cv2.putText(pair,n,(5,18),0,.6,(0,0,255),2); dbg.append(pair)
    print(n,'band',round(hmean),'x',x0,x1)
w=max(d.shape[1] for d in dbg)
cv2.imwrite(F+'texdbg.jpg',np.vstack([cv2.copyMakeBorder(d,0,4,0,w-d.shape[1],cv2.BORDER_CONSTANT) for d in dbg]))
