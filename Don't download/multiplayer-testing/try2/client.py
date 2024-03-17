#!/usr/bin/env python

import asyncio
import websockets

async def hello(uri, x, y, Player, Type=True, Payload=[]):
    #uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        payload = [Type, x, y, Player, Payload]
        await websocket.send(str(payload))
        print(f">>> {payload}")
        #greeting = await websocket.recv()
        #print(f"<<< {greeting}")
        #await asyncio.Future()
def SendPlayerData(uri, x, y, Player, Type=True, Payload=[]):
    asyncio.run(hello(uri, x, y, Player, Type, Payload))
if __name__ == "__main__":
    asyncio.run(hello("ws://localhost:8765", 0, 0, 1, True))