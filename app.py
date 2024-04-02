import asyncio

import tasks.video_analyse  # noqa
from tasks import start_handling


if __name__ == "__main__":
    asyncio.run(start_handling())




