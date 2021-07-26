import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 

img = cv.imread("./a.png")


blank = np.zeros(img.shape[:2],dtype = 'uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray_hist = cv.calcHist([gray],[0],None,[256],[0,256] )

plt.plot(gray_hist)
plt.title("gray")
plt.xlabel('bins')
plt.ylabel("n of pixels")
plt.xlim([0,256])
plt.show()


cv.imshow("and",gray)
cv.waitKey(0)