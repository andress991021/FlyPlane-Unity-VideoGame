import cv2
from detector import HandDetector     
     
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
hand_detector = HandDetector()
    
while(True):      

    
    ret, frame = cap.read()
    if(ret == False):
        break
    
    frame = hand_detector.find_hand(frame)
    cv2.imshow('mask',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

        
cap.release()     
cv2.destroyAllWindows()
  