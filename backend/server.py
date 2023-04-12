#!/usr/bin/env python

import asyncio
import websockets

async def redirect_time(websocket, path):
    async with websockets.connect('ws://localhost:8766') as forward_websocket:
        async for time in websocket:
            print(f"Script B received time: {time}")
            await forward_websocket.send(time)

start_server = websockets.serve(redirect_time, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()