import cv2 as cv 

capture = cv.VideoCapture("./videoname")

while True :
    isframe,frame = capture.read()

    cv.imshow("video",frame)

    if cv.waitKey(20) & 0xFF == ord('a') :
        break

capture.release()
cv.destroyAllWindows()

