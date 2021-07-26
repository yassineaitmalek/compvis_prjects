import numpy as np  
import cv2 as cv  

def resize_img(frame,scale=0.5) :
    w = int(frame.shape[0]*scale)
    h = int(frame.shape[1]*scale)

    return cv.resize(frame,(w,h),interpolation=cv.INTER_AREA)

people = ['a','b']
haar_cascade = cv.CascadeClassifier("./haar_faces.xml")

# features = np.load('./features.npy')
# labels = np.load('./labels.npy')

face_rec = cv.face.LBPHFaceRecognizer_create()
face_rec.read("./face_trained.yml")

img = cv.imread("./c.jpg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face_rectangle = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
for (x,y,w,h) in face_rectangle : 
    faces_roi = gray[y:y+h,x:x+w]

    label,confidence = face_rec.predict(faces_roi)
    print(f"label = {people[label]} whit confidence of {confidence}")
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=3)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)

cv.imshow("text",resize_img( img))

cv.waitKey(0)
