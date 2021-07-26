import cv2 as cv

img = cv.imread("./a.png")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#  simple thresholding

threshold , thresh = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY)

threshold , thresh = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY_INV)

#  adapting thresholding
adapt = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)



cv.imshow("image",adapt)

cv.waitKey(0)