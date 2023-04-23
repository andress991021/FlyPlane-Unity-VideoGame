import asyncio
import datetime
import websockets

async def time(websocket, path):
    print('starting')
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print(now)
        await websocket.send(now)
        await asyncio.sleep(3)

async def main():
    async with websockets.serve(time, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())