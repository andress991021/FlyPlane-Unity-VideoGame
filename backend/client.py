#!/usr/bin/env python
from websockets.sync.client import connect
import time
import cv2
from computer_vision import HandDetector,Dynamics  
from settings import settings

# Open the video capture using the camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   

# Initialize the hand detection class
hand_detector = HandDetector()
dynamics =  Dynamics()

# Continuously detect the hand position and send it through websockets
def stream_hand_position():
    # Connect to websocket mediator
    with connect(f"ws://localhost:8000") as websocket:
        for i in range(5000):
            # Capture the image
            ret, frame = cap.read()
            frame = cv2.flip(frame,1)
            
            # Detect the hand and its principal keypoints
            frame = hand_detector.find_hand(frame)   
            main_keypoint = hand_detector.find_main_keypoint(frame, False) 
            
            # If a hand position is found, send it through websockets
            if main_keypoint is not None:
                dynamics.add_vector(main_keypoint)
                vx,vy = dynamics.calculate_velocity()
                str_position = f'{vx:.4f},{vy:.4f}'
                print(f'Sending hand position: {str_position}')
                websocket.send(str_position)
            
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
stream_hand_position()