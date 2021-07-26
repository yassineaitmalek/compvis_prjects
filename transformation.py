import cv2 as  cv 
import numpy as np

img = cv.imread("./a.png")

# translation
def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]]) 
    dim = (img.shape[0],img.shape[1])

    return cv.warpAffine(img,transmat,dim)

# translated = translate(img,100,100)

# rotation
def rotate(img,ang,rotpt=None):
    (h,w)=img.shape[:2]

    if rotpt is None :
        rotpt = (w//2,h//2)
    rotmat = cv.getRotationMatrix2D(rotpt,ang,1)
    dim = (w,h)
    return cv.warpAffine(img,rotmat,dim)

# rotated = rotate(img,45)

# flip
# flip = cv.flip(img,-1)


cv.imshow("image",img)
cv.waitKey(0)
