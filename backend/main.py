import cv2
from detector import HandDetector     
     
class Dynamics():
    def __init__(self):
        self.vector_old = None
        self.vector_current = None
        
    def update(self,new_vector):
        if self.vector_old is None and self.vector_current is None:
            self.vector_current = new_vector
            return
        
        self.vector_old = self.vector_current
        self.vector_current = new_vector
        
    def calculate_velocity(self):
        if self.vector_old is None or self.vector_current is None:
            return (0,0)
        dx = self.vector_current['x']-self.vector_old['x']
        dy = self.vector_current['y']-self.vector_old['y']
        return (round(dx,1),round(dy,1) )
    
    def is_empty(self):
        return self.vector_old is None and self.vector_current is None
            
     
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
hand_detector = HandDetector()
dynamics = Dynamics()
    
while(True):      

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    if(ret == False):
        break
    
    frame = hand_detector.find_hand(frame)   
    vertex = hand_detector.find_main_keypoint(frame) 
    if(vertex): 
        #print(vertex)
        dynamics.update(vertex)
        print(dynamics.calculate_velocity())
     
    cv2.imshow('mask',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break 
        
cap.release()     
cv2.destroyAllWindows()
  