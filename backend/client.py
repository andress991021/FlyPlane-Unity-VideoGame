#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect
import time
import cv2
from computer_vision import HandDetector,Dynamics    
from settings import settings

host =  settings.host
port = settings.port


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
hand_detector = HandDetector()
dynamics = Dynamics()

def streaming():
    with connect(f"ws://{host}:{port}") as websocket:
        for i in range(500):
            ret, frame = cap.read()
            frame = cv2.flip(frame,1)
            

            frame = hand_detector.find_hand(frame)   
            vector = hand_detector.find_main_keypoint(frame,False) 
            
            if vector is not None:
                
                x = vector['x']
                x_formatted = f'{x:.2f}'
                print(x_formatted)
                websocket.send(x_formatted)
            
            cv2.imshow('mask',frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break 
            
            time.sleep(0)
            

        cap.release()     
        cv2.destroyAllWindows()

streaming()