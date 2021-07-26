import cv2 as cv

img = cv.imread("./a.png")

#to gray_scale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)


# blur
# blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

#edge cascade 
# canny = cv.Canny(img,125,175)

# dilating image
# dilated = cv.dilate(canny,(3,3),iterations=5)

# eroding
# eroded = cv.erode(dilated,(7,7),iterations=5)

# resize
# resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)

# crop
# crop = img[0:200,200:500]


cv.imshow("image",img)

cv.waitKey(0)