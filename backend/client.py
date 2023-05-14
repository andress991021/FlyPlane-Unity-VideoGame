#!/usr/bin/env python
from websockets.sync.client import connect
import time
import cv2
from computer_vision import HandDetector,Dynamics  
from settings import settings
import json

# Open the video capture using the camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   

# Initialize the hand detection class
hand_detector = HandDetector()
dynamics =  Dynamics()

# Continuously detect the hand position and send it through websockets
def realtime_hand_detection():
    # Connect to websocket mediator
    with connect(f"ws://localhost:8000") as websocket:
        for i in range(5000):
            # Capture the image
            ret, frame = cap.read()
            frame = cv2.flip(frame,1)
            
            # Detect the hand and its principal keypoints
            frame = hand_detector.find_hand(frame)   
            hand_position = hand_detector.find_main_keypoint(frame, False) 
            # If a hand position is found, send it through websockets
            if hand_position is not None:
                #Calculate and destructuring position and velocity
                dynamics.add_vector(hand_position)
                px,py = hand_position
                vx,vy = dynamics.calculate_velocity()
                
                #Enconde message in json format
                msg = dict(vx=vx,vy=vy,px=px,py=py)
                encode_msg = json.dumps(msg)
                
                #Send message
                print(f'Sending hand position: {encode_msg}')
                websocket.send(encode_msg)
            
            # Show the hand detection mask
            cv2.imshow('Hand Detection Mask', frame)
            
            # Exit if the 'Esc' key is pressed
            if cv2.waitKey(1) & 0xFF == 27:
                break 
            
            time.sleep(0)
        
        # Release the video capture and destroy the window
        cap.release()     
        cv2.destroyAllWindows()

# Start streaming the hand position
realtime_hand_detection()