from datetime import datetime, timedelta
from typing import Dict, Tuple
from numpy import array
     
class Dynamics():
    def __init__(self):
        self.vector_old: array = None
        self.vector_current: array = None
        self.time_old: datetime = None
        self.time_current: datetime = None
        
    def add_vector(self,new_vector:array):
        
        self.vector_old = self.vector_current
        self.time_old = self.time_current
        
        self.vector_current = new_vector
        self.time_current = datetime.now()
        
        
    def calculate_velocity(self):
        if self.vector_old is None or self.vector_current is None:
            return (0,0)
        dt = (self.time_current - self.time_old).total_seconds()
        vx,vy = (self.vector_current- self.vector_old)/dt
        return vx,vy
    
    def is_empty_vectors(self):
        return self.vector_old is None and self.vector_current is None