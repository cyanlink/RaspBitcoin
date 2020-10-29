import websockets
import asyncio
import json
from .rblib import rbimage

ws_uri = "wss://ws.blockchain.info/inv"

# determine if this addr is already used, and return a unused one
async def get_unused_address():
    pass


# use WS to wait for responds
async def subscribe_addr():
    pass


async def unsubscribe_addr():
    pass


async def polling():
    async with websockets.connect(ws_uri) as websocket:
        while True:
            tx = input()
            await websocket.send()


async def keep_alive(socket: websockets.WebSocketClientProtocol):
    while True:
        ping = input('{"op":"ping"}')
        socket.send(ping)
        await asyncio.sleep(3600)


def main():
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
