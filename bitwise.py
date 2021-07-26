import cv2 as cv
import numpy as np 

img = cv.imread("./a.png")


blank = np.zeros((500,500,3),dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(),(0,0),(250,250),(0,255,0),thickness=-1)
circle = cv.circle(blank.copy(),(250,250),100,(0,255,0),thickness=-1)

bitwise_and = cv.bitwise_and(rectangle,circle)

bitwise_or = cv.bitwise_or(rectangle,circle)

bitwise_xor = cv.bitwise_xor(rectangle,circle)

cv.imshow("and",bitwise_xor)
cv.waitKey(0)