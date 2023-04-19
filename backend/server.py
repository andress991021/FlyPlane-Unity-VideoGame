import asyncio
import websockets
from settings import settings


async def handle_time(websocket, path):
    #async with websockets.connect(f'ws://localhost:8766') as websocket2:
    async for msg in websocket:
        print(msg)
        #await websocket2.send(time)

asyncio.get_event_loop().run_until_complete(websockets.serve(handle_time, settings.host, settings.port_bridge))
asyncio.get_event_loop().run_forever()