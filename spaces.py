import cv2 as cv
import matplotlib.pyplot as plt 


img = cv.imread("./a.png")

# plt.imshow(img)
# plt.show()

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# BGR to LAB

lab =  cv.cvtColor(img,cv.COLOR_BGR2LAB)

lab_reverse =   cv.cvtColor(lab,cv.COLOR_Lab2BGR)

#  BGR TO RGB
rgb  =  cv.cvtColor(img,cv.COLOR_BGR2RGB)

cv.imshow("image",lab_reverse)

cv.waitKey(0)