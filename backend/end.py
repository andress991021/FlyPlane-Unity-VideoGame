#!/usr/bin/env python

import asyncio
import websockets

async def receive_time():
    async with websockets.connect('ws://localhost:8766') as websocket:
        while True:
            time = await websocket.recv()
            print(f"Script C received time: {time}")

asyncio.get_event_loop().run_until_complete(receive_time())