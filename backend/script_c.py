import asyncio
import websockets

async def handle_time(websocket, path):
    async for time in websocket:
        print(f'Received time from Script B: {time}')

asyncio.get_event_loop().run_until_complete(websockets.serve(handle_time, '192.168.1.106', 8001))
asyncio.get_event_loop().run_forever()