import cv2 as cv

img = cv.imread("./a.png")


#  avrage blurring
avg = cv.blur(img,(7,7))

#  gaussian
gauss = cv.GaussianBlur(img,(7,7),0)

# median 
median = cv.medianBlur(img,3)

#  bilateral
bi = cv.bilateralFilter(img,15,15,15)

cv.imshow("image",bi)

cv.waitKey(0)