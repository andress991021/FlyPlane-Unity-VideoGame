import asyncio
import websockets

#Manage communication between hand detection and Unity for movement control
'''
This code is responsible for managing the communication between the hand detection module and Unity,
in order to enable hand-based movement control in a Unity application.
'''

async def mediator(client_ws, path):
    counter = 0
    # Connect to the server WebSocket at ws://localhost:8765/time
    async with websockets.connect('ws://localhost:8765/time', ping_interval=None) as unity_ws:
        # Loop over incoming messages from the client WebSocket
        async for message in client_ws:
            # Increment the message counter
            counter += 1
            # Send the message to the server WebSocket
            await unity_ws.send(message)

# Start a WebSocket server on localhost:8000
asyncio.get_event_loop().run_until_complete(
    websockets.serve(mediator, 'localhost', 8000))

# Run the event loop indefinitely
asyncio.get_event_loop().run_forever()