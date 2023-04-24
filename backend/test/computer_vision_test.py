import cv2
from detector import HandDetector     
from dynamics import Dynamics
            
     
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
hand_detector = HandDetector()
dynamics = Dynamics()
    
while(True):      

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    if(ret == False):
        break
    
    frame = hand_detector.find_hand(frame)   
    vector = hand_detector.find_main_keypoint(frame,False) 
    if vector: 
        dynamics.add_vector(vector)
        vx,vy =dynamics.calculate_velocity()
        output = '{:.1f}'.format(vx)+' , '+'{:.1f}'.format(vy)
        #print('{:.1f}'.format(vx),'{:.1f}'.format(vy))
     
    cv2.imshow('mask',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break 
        
cap.release()     
cv2.destroyAllWindows()
  