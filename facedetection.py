import cv2 as cv

def resize_img(frame,scale=0.3) :
    w = int(frame.shape[0]*scale)
    h = int(frame.shape[1]*scale)

    return cv.resize(frame,(w,h),interpolation=cv.INTER_AREA)




img = cv.imread("./b.jpg")
cv.imshow('image',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier("./haar_faces.xml")

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)

print(len(faces_rect))

for (x,y,w,h) in faces_rect : 
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
  
cv.imshow('image',resize_img(img))
cv.waitKey(0)