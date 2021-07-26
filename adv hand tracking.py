import cv2 as cv 
import mediapipe as mp 
import time as t 


capture = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
draw = mp.solutions.drawing_utils

pt = 0
ct = 0

while True :
    isframe,img = capture.read()
    imgrgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    result = hands.process(imgrgb)
    # print(result.multi_hand_landmarks)
    
    if result.multi_hand_landmarks : 
        for handlm in result.multi_hand_landmarks :
            for id,lm in enumerate(handlm.landmark) :
                # print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)

                if id == 4 : 
                    cv.circle(img,(cx,cy),15,(0,255,0),cv.FILLED)

            draw.draw_landmarks(img,handlm,mphands.HAND_CONNECTIONS)
    
    ct = t.time()
    fps = 1/(ct-pt)
    pt = ct

    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=6)
    cv.imshow("video",img)

    if cv.waitKey(20) & 0xFF == ord('a') :
        break

capture.release()
cv.destroyAllWindows()

