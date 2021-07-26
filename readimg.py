import cv2 as cv

img = cv.imread("./a.png")

def resize_img(frame,scale=0.5) :
    w = int(frame.shape[0]*scale)
    h = int(frame.shape[1]*scale)

    return cv.resize(frame,(w,h),interpolation=cv.INTER_AREA)



cv.imshow('screen',resize_img(img))

# cv.imshow('screen',img)

cv.waitKey(0)