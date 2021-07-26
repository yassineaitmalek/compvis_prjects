import cv2 as cv
import numpy as np
from numpy.core.arrayprint import dtype_short_repr 

blank = np.zeros((500,500,3),dtype = 'uint8')

# blank[:] = 0,255,0

# cv.imshow("green",blank)

# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=3)
# cv.imshow("rectangle",blank)

# cv.circle(blank,(250,250),100,(0,255,0),thickness=3)
# cv.imshow("circle",blank)

# cv.line(blank,(0,0),(250,250),(0,255,0),thickness=1)
# cv.imshow("line",blank)

cv.putText(blank,'hi',(250,250),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=3)
cv.imshow("text",blank)

cv.waitKey(0)
