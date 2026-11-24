import cv2, numpy as np, json, os
B='/home/user/ebooks/carrusel-imperia/assets/navidad/'
F='/tmp/claude-0/-home-user-ebooks/578aafb8-e622-52a6-8fca-47556ff481b3/scratchpad/fix/'
C={'m-p':((520,1245,715,1372),'dark'),'m-s2':((518,1245,712,1360),'dark'),'m-s3':((170,1195,430,1350),'dark'),'m-s4':((605,1200,765,1310),'dark'),
'c-p':((395,1218,542,1330),'dark'),'c-s2':((270,1198,430,1316),'dark'),'c-s3':((742,1168,905,1342),'dark'),'c-s4':((303,1222,483,1352),'dark'),
'v-p':((160,818,268,935),'bright'),'v-s3':((160,818,268,935),'bright'),
's-p':((512,1152,708,1272),'lowsat'),'s-s2':((550,1058,774,1196),'lowsat'),'s-s3':((624,855,986,1140),'lowsat')}
def src(n):
    for p in [B+'tex/'+n+'.png',B+'orig/'+n+'.png',B+'orig/'+n+'.jpg']:
        if os.path.exists(p): return p
def order(p):
    p=np.array(p,dtype=np.float32); s=p.sum(1); d=np.diff(p,axis=1).ravel()
    return np.array([p[np.argmin(s)],p[np.argmin(d)],p[np.argmax(s)],p[np.argmax(d)]],dtype=np.float32)
res={}; tiles=[]
for n,((x0,y0,x1,y1),mode) in C.items():
    im=cv2.imread(src(n)); sub=im[y0:y1,x0:x1]
    g=cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY).astype(np.float32); hsv=cv2.cvtColor(sub,cv2.COLOR_BGR2HSV)
    b=cv2.blur(g,(9,9))
    if mode=='dark':
        t=(np.percentile(b,10)+np.percentile(b,80))/2; m=(b<t)
    elif mode=='bright':
        t=(np.percentile(b,20)+np.percentile(b,95))/2; m=(b>t)
    else:
        sb=cv2.blur(hsv[...,1].astype(np.float32),(9,9)); t=(np.percentile(sb,10)+np.percentile(sb,75))/2
        m=(sb<t)|(b<np.percentile(b,8))
    m=m.astype(np.uint8)*255
    m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
    cs,_=cv2.findContours(m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE); c=max(cs,key=cv2.contourArea)
    hull=cv2.convexHull(c); ap=cv2.approxPolyDP(hull,0.04*cv2.arcLength(hull,True),True)
    q=order(ap.reshape(-1,2)) if len(ap)==4 else order(cv2.boxPoints(cv2.minAreaRect(c)))
    res[n]=(q+[x0,y0]).tolist()
    vis=im.copy(); cv2.polylines(vis,[np.int32(res[n])],True,(0,255,0),1)
    t2=vis[max(0,y0-30):y1+30,max(0,x0-40):x1+40]; t2=cv2.resize(t2,(360,int(360*t2.shape[0]/t2.shape[1])))
    cv2.putText(t2,n,(4,16),0,.5,(0,0,255),2); tiles.append(t2)
json.dump(res,open(F+'quads2.json','w'),indent=1)
hm=max(t.shape[0] for t in tiles); tiles=[cv2.copyMakeBorder(t,0,hm-t.shape[0]+4,0,4,cv2.BORDER_CONSTANT) for t in tiles]
tiles+= [np.zeros_like(tiles[0])]*((5-len(tiles)%5)%5)
cv2.imwrite(F+'det2.jpg',np.vstack([np.hstack(tiles[i:i+5]) for i in range(0,len(tiles),5)]))
