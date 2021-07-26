import cv2 as cv 
import mediapipe as mp 
import time as t 


capture = cv.VideoCapture(0)
pt = 0
ct = 0
mpface = mp.solutions.face_mesh
face = mpface.FaceMesh(min_detection_confidence=0.5,max_num_faces = 1,min_tracking_confidence=0.5)
draw = mp.solutions.drawing_utils

while True :
    isframe,img = capture.read()
    imgrgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    results = face.process(img)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        draw.draw_landmarks(
            image=img,
            landmark_list=face_landmarks,
            connections=mpface.FACE_CONNECTIONS,
            landmark_drawing_spec=draw.DrawingSpec(thickness=1, circle_radius=1),
            connection_drawing_spec=draw.DrawingSpec(thickness=1, circle_radius=1))
          
    ct = t.time()
    fps = 1/(ct-pt)
    pt = ct

    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=6)
    cv.imshow("video",img)

    if cv.waitKey(1) & 0xFF == ord('a') :
        break

capture.release()
cv.destroyAllWindows()
