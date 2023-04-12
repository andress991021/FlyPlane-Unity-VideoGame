import asyncio
import websockets
import datetime

async def send_time():
    connected = False
    while not connected:
        try:
            async with websockets.connect('ws://localhost:8765') as websocket:
                connected = True
                while True:
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Script A sent time: {current_time}")
                    await websocket.send(current_time)
                    await asyncio.sleep(3)
        except Exception as e:
            print(f"Script A could not connect: {str(e)}. Retrying in 5 seconds...")
            await asyncio.sleep(5)

asyncio.get_event_loop().run_until_complete(send_time())