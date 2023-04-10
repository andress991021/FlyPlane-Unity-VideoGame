#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect
import time
import cv2
from detector import HandDetector     
from dynamics import Dynamics

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
hand_detector = HandDetector()
dynamics = Dynamics()

def hello():
    with connect("ws://localhost:8765") as websocket:
           
        websocket.send("Hello world!")
        #message = websocket.recv()
        #print(f"Received: {message}")


for i in range(10):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    

    frame = hand_detector.find_hand(frame)   
    vector = hand_detector.find_main_keypoint(frame,False) 
    print(vector)
    
    cv2.imshow('mask',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break 
    
    time.sleep(1)
    #hello()

cap.release()     
cv2.destroyAllWindows()

