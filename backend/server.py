#!/usr/bin/env python

import asyncio
from websockets.server import serve
import random

async def echo(websocket):
    async for message in websocket:
        print(message)
        #msg = random.choice(["A", "B","C"])
        #await websocket.send(msg)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())