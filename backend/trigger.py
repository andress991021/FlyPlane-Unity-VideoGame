import asyncio
import websockets


async def trigger():
    input("Press Enter to start communication...")
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send("Start communication")

asyncio.get_event_loop().run_until_complete(trigger())