import asyncio
import websockets

import tasks.video_analyse  # noqa
from tasks import start_handling
from grifon.log import get_logger

logger = get_logger(__name__)


async def echo(websocket, path):
    async for message in websocket:
        print("Получено сообщение от клиента:", message)
        await websocket.send("Эхо: " + message)


async def main():
    start_server = websockets.serve(echo, "localhost", 8765)

    consumer_task = asyncio.create_task(start_handling())

    await asyncio.gather(start_server, consumer_task, )


if __name__ == "__main__":
    logger.info(f'Init recommendation manager')
    asyncio.run(main())




