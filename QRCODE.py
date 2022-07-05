import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap=cv2.VideoCapture(0)
while True:
    succ,frame=cap.read()

    for co in decode(frame):
        #3print(co.rect)
        mydata = co.data.decode('utf-8')
        pts2 = co.rect
        x,y,w,h=co.rect
        #pts=np.array([co.polygon],np.int32)
        #pts=pts.reshape((-1,1,2))
        #cv2.polylines(frame,[pts],True,(255,0,255),6)


        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(frame,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,235),2)
        #print(mydata)
    cv2.imshow('farme',frame)
    cv2.waitKey(1)
