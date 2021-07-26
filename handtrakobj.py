import cv2 as cv 
import mediapipe as mp 
import time as t

class HandTrack():

    def __init__(self,mode = False,maxHand = 2,detectiocon = 0.5,trackCon = 0.5):
        self.mode = mode
        self.maxHand = maxHand
        self.detectiocon = detectiocon
        self.trackCon = trackCon

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands( self.mode,self.maxHand,self.detectiocon,self.trackCon)
        self.draw = mp.solutions.drawing_utils    


    
    def findHand(self,img,draw = True):
        imgrgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.result = self.hands.process(imgrgb)
        if self.result.multi_hand_landmarks :    
            for handlm in self.result.multi_hand_landmarks :
                if draw :
                    self.draw.draw_landmarks(img,handlm,self.mphands.HAND_CONNECTIONS)
                   
        return img 

    def findPosition(self,img,handn = 0,draw = False) :
        lmlist = []
        if self.result.multi_hand_landmarks :  
            hand =  self.result.multi_hand_landmarks[handn]
            for id,lm in enumerate(hand.landmark) :       
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw : 
                    cv.circle(img,(cx,cy),15,(0,255,0),cv.FILLED)
        return lmlist

  

def main() :
    
    pt = 0
    ct = 0
    capture = cv.VideoCapture(0)
    ht = HandTrack()
    while True :
        isframe,img = capture.read()
        img = ht.findHand(img)
        lmlist = ht.findPosition(img)
        if (len(lmlist) != 0 ) :
            print(lmlist[4])
        
        ct = t.time()
        fps = 1/(ct-pt)
        pt = ct

        cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=6)
        cv.imshow("video",img)

        if cv.waitKey(20) & 0xFF == ord('a') :
            break

    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__" :
    main()