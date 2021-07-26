import os
import numpy as np  
import cv2 as cv  




people = ['a','b']

dir = "C:\\Users\\yf\\Desktop\\openCV\\Train"

features = []
labels  = []
haar_cascade = cv.CascadeClassifier("./haar_faces.xml")
def create_train():
    for p in people :
        path = os.path.join(dir,p)
        label = people.index(p)

        for img in os.listdir(path) :
            img_path =  os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces_rect : 
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
features = np.array(features,dtype='object')
labels = np.array(labels)

face_rec = cv.face.LBPHFaceRecognizer_create()

face_rec.train(features,labels)

face_rec.save("face_trained.yml")
np.save("features.npy",features)
np.save("labels.npy",labels)