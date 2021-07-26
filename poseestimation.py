import cv2 as cv 
import mediapipe as mp 
import time as t 


capture = cv.VideoCapture(0)
pt = 0
ct = 0
mppose = mp.solutions.pose  
pose = mppose.Pose()
draw = mp.solutions.drawing_utils

while True :
    isframe,img = capture.read()
    imgrgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)


    result = pose.process(imgrgb)
    if result.pose_landmarks : 

        draw.draw_landmarks(img,result.pose_landmarks,mppose.POSE_CONNECTIONS)



    ct = t.time()
    fps = 1/(ct-pt)
    pt = ct

    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=6)
    cv.imshow("video",img)

    if cv.waitKey(1) & 0xFF == ord('a') :
        break

capture.release()
cv.destroyAllWindows()
