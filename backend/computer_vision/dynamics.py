from datetime import datetime, timedelta
from typing import Dict, Tuple
import numpy as np
from numpy import array
     
class Dynamics():
    def __init__(self):
        self.position = []
        self.time = []
        self.velocity = []
        
    def add_vector(self,new_vector:array):
        self.position.append(new_vector)
        self.time.append(datetime.now()) 
        
        
    def calculate_velocity(self):
        if len(self.position)<3:
            return (0,0)
        dt_1 = (self.time[-1]- self.time[-2]).total_seconds()
        dt_2 = (self.time[-2]- self.time[-3]).total_seconds()
        
        v_1 = (self.position[-1]- self.position[-2])/dt_1
        v_2 = (self.position[-2]- self.position[-3])/dt_2
        vx,vy = v_1*0.6+v_2*0.4
        return vx,vy
    
