import cv2
from detector import HandDetector     
from dynamics import Dynamics
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio

app = FastAPI()

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   
hand_detector = HandDetector()
dynamics = Dynamics()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Hand Velocity</title>
    </head>
    <body>
        <h1>Hand Velocity</h1>
        <div id="output"></div>
        <script>
            var socket = new WebSocket("ws://localhost:8000/ws");
            socket.onmessage = function(event) {
                document.getElementById("output").innerHTML = event.data;
            };
        </script>
    </body>
</html>
"""

# Create a list to store all active websocket connections
connections = []

# Define a function to send the current velocity to all active connections
async def send_velocity():
    while True:
        if len(connections) > 0:
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
                
                for connection in connections:
                    await connection.send_text(output)
        
        await asyncio.sleep(0.1)

# Define a websocket endpoint that adds new connections to the list
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)

    try:
        # Wait for the connection to close
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        # Remove the connection from the list when it closes
        connections.remove(websocket)

# Define a route to serve the HTML page
@app.get("/")
async def get():
    return HTMLResponse(content=html, status_code=200)

# Start the send_date task in the background when the app starts
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(send_velocity())


    

