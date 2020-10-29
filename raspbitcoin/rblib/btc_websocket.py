import websockets
import asyncio

async def sub_address(address):
    pass

async def keep_alive(websocket):
    while True:
        # TODO: ping the websocket
        asyncio.sleep(20)
