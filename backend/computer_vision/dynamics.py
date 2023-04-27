from datetime import datetime, timedelta
from typing import Dict, Tuple

     
class Dynamics():
    def __init__(self):
        self.vector_old: Dict[str, float] = None
        self.vector_current: Dict[str, float] = None
        self.time_old: datetime = None
        self.time_current: datetime = None
        
    def add_vector(self,new_vector:Dict[str, float]):
        if self.is_empty_vectors():
            self.vector_current = new_vector
            self.time_current = datetime.now()
            return
        
        self.vector_old = self.vector_current
        self.vector_current = new_vector
        
        self.time_old = self.time_current
        self.time_current = datetime.now()
        
    def calculate_velocity(self):
        if self.vector_old is None or self.vector_current is None:
            return (0,0)
        dt = (self.time_current - self.time_old).total_seconds()
        dx = (self.vector_current['x']-self.vector_old['x'])/dt
        dy = (self.vector_current['y']-self.vector_old['y'])/dt
        return (dx,dy)
    
    def is_empty_vectors(self):
        return self.vector_old is None and self.vector_current is None