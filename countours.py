import cv2 as cv
import numpy as np 



img = cv.imread("./a.png")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175)


blank = np.zeros(img.shape,dtype = 'uint8')
ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
countours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# countours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(countours))

draw = cv.drawContours(blank,countours,-1,(0,0,255),1)

cv.imshow("image",draw)

cv.waitKey(0)