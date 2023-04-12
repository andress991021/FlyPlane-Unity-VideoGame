import asyncio
import websockets

async def receive_time():
    connected = False
    while not connected:
        try:
            async with websockets.connect('ws://localhost:8766') as websocket:
                connected = True
                while True:
                    time = await websocket.recv()
                    print(f"Script C received time: {time}")
        except Exception as e:
            print(f"Script C could not connect: {str(e)}. Retrying in 5 seconds...")
            await asyncio.sleep(5)

asyncio.get_event_loop().run_until_complete(receive_time())