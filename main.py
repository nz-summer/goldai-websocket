import asyncio
import json
import os
import websockets

latest_market_data = {}

async def handler(websocket):

    global latest_market_data

    print("Client Connected")

    async for message in websocket:

        latest_market_data = json.loads(message)

        print("Received:")
        print(latest_market_data)

PORT = int(os.environ.get("PORT", 8765))

async def main():

    server = await websockets.serve(
        handler,
        "0.0.0.0",
        PORT
    )

    print(f"WebSocket Server Running on Port {PORT}")

    await server.wait_closed()

asyncio.run(main())