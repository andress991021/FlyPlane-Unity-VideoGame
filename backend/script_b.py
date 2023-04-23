import asyncio
import websockets



async def handle_time(websocket, path):
    x = 0
    async with websockets.connect('ws://localhost:8765/time',ping_interval=None) as websocket2:
        async for time in websocket:
            print(f'Received time from client: {time} / times ({x})')
            x=x+1
            await websocket2.send(time)

asyncio.get_event_loop().run_until_complete(websockets.serve(handle_time, 'localhost', 8000))
asyncio.get_event_loop().run_forever()