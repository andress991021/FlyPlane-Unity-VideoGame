from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio
import datetime

app = FastAPI()

# Create a list to store all active websocket connections
connections = []


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


async def send_date():
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for connection in connections:
            await connection.send_text(now)
        await asyncio.sleep(10)

# Define a websocket endpoint that adds new connections to the list
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        # Wait for the connection to close
        while True:
            await websocket.receive_text()
    finally:
        # Remove the connection from the list when it closes
        connections.remove(websocket)

# Start the send_date task in the background when the app starts
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(send_date())