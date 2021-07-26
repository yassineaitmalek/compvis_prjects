import cv2 as cv
import numpy as np  
import time as t 
import math as m
import handtrakobj as ht
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
###################################
wc , hc = 640 , 480

###################################
pt = 0
ct = 0
capture = cv.VideoCapture(0)
capture.set(3,wc)
capture.set(4,hc)
det = ht.HandTrack(detectiocon=0.8)



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volrange = volume.GetVolumeRange()


minvol = volrange[0]
maxvol = volrange[1]

volbar = 400
volper = 0

while True :
    isframe,img = capture.read()
   
    img = det.findHand(img)

    l = det.findPosition(img)

    if len(l) != 0:
        x1 , y1  =  l[4][1],l[4][2]
        x2 , y2  =  l[8][1],l[8][2]

        cx , cy  = (x1 + x2)//2 , (y2 + y1)//2 

        cv.circle(img,(x1,y1),5,(255,0,255),cv.FILLED)
        cv.circle(img,(x2,y2),5,(255,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),3)

        cv.circle(img,(cx , cy),5,(255,0,255),cv.FILLED)

        lenght = m.hypot(x2 - x1,y2 - y1)
        print(lenght)

        ## hand range 30 -- 150
        # volume range -65 -- 0

        vol = np.interp(lenght,[30,150],[minvol,maxvol])
        volbar = np.interp(lenght,[30,150],[400,150])
        volper = np.interp(lenght,[30,150],[0,100])
        volume.SetMasterVolumeLevel(vol, None)

  


    cv.rectangle(img,(50,150),(85,400),(0,255,0),thickness=3)  
    cv.rectangle(img,(50,int(volbar)),(85,400),(0,255,0),cv.FILLED)  
    cv.putText(img,str(int(volper))+"%",(40,450),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=6)


    ct = t.time()
    fps = 1/(ct-pt)
    pt = ct
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=6)
    cv.imshow("video",img)
    if cv.waitKey(1) & 0xFF == ord('a') :
        break

capture.release()
cv.destroyAllWindows()
