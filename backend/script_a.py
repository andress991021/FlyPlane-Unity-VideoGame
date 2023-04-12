import asyncio
import websockets
import time

async def send_time():
    async with websockets.connect('ws://localhost:8000') as websocket:
        while True:
            current_time = time.strftime("%H:%M:%S", time.gmtime())
            print(f'Sending time: {current_time}')
            await websocket.send(current_time)
            await asyncio.sleep(3)

asyncio.get_event_loop().run_until_complete(send_time())