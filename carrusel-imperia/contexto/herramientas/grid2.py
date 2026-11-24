import cv2, sys, numpy as np
O='/home/user/ebooks/carrusel-imperia/assets/navidad/orig/'
out=sys.argv[1]; specs=sys.argv[2:]; tiles=[]
for sp in specs:
    n,y0,y1=sp.split(':'); y0=int(y0); y1=int(y1)
    im=cv2.imread(O+n)[y0:y1].copy(); H,W=im.shape[:2]
    for x in range(0,W,25):
        c=(0,0,255) if x%100==0 else (0,200,255); cv2.line(im,(x,0),(x,H),c,1)
        if x%100==0: cv2.putText(im,str(x),(x+2,14),0,.45,(255,255,0),1)
    for y in range(((y0+24)//25)*25,y1,25):
        Y=y-y0; c=(0,0,255) if y%100==0 else (0,200,255); cv2.line(im,(0,Y),(W,Y),c,1)
        if y%100==0: cv2.putText(im,str(y),(2,Y-2),0,.45,(255,255,0),1)
    cv2.putText(im,n,(W//2,H-10),0,.8,(255,0,255),2)
    tiles.append(cv2.resize(im,(1000,int(1000*H/W))))
cv2.imwrite(out,np.vstack(tiles))
