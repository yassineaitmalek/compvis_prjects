import cv2 as cv
import numpy as np


img = cv.imread("./a.png")
blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)

merge = cv.merge([r,b,r])

merge_b = cv.merge([b,blank,blank])

cv.imshow("image",merge_b)

cv.waitKey(0)