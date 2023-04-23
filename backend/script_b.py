import asyncio
import websockets

async def handle_time(websocket, path):
    async with websockets.connect('ws://192.168.1.106:8001',ping_interval=None) as websocket2:
        async for time in websocket:
            print(f'Received time from client: {time}')
            await websocket2.send(time)

asyncio.get_event_loop().run_until_complete(websockets.serve(handle_time, '192.168.1.106', 8000))
asyncio.get_event_loop().run_forever()