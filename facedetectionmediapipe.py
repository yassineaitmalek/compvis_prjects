import cv2 as cv 
import mediapipe as mp 
import time as t 


capture = cv.VideoCapture(0)
pt = 0
ct = 0
mpface = mp.solutions.face_detection  
face = mpface.FaceDetection()
draw = mp.solutions.drawing_utils

while True :
    isframe,img = capture.read()
    imgrgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)


    result = face.process(imgrgb)
    if result.detections : 
        for id,det in enumerate(result.detections ) :
            # draw.draw_detection(img,det)
            # print(id,det)
            # print(det.score)
            # print(det.location_data.relative_bounding_box)

            bboxc = det.location_data.relative_bounding_box
            h,w,c = img.shape
            bbox = int(bboxc.xmin*w),int(bboxc.ymin*h),int(bboxc.width*w),int(bboxc.height*h)

            cv.rectangle(img,bbox,(0,255,0),thickness=3)
            cv.putText(img,str(int(det.score[0]*100))+"%",(bbox[0],bbox[1]-20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=6)
    ct = t.time()
    fps = 1/(ct-pt)
    pt = ct

    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=6)
    cv.imshow("video",img)

    if cv.waitKey(1) & 0xFF == ord('a') :
        break

capture.release()
cv.destroyAllWindows()
