#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")
    orpayload = eval(name)
    if orpayload[0]:
        with open("s-playpos.txt", "rt")  as f:
            fc = f.read()
            print(fc)
    #greeting = f"Hello {name}!"

    #await websocket.send(greeting)
    #print(f">>> {greeting}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())