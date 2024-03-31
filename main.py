import asyncio

from config import settings
from grifon.mqbroker.kafka_client import KafkaClient
from tasks.video_analyse import get_recommendations

kafka_client = KafkaClient(f"localhost:{settings.KAFKA_CLIENT_PORT}")


kafka_client.register_topic_handler(settings.VIDEO_ANALYSIS_TOPIC, get_recommendations)


async def main():
    await kafka_client.start_handling()


if __name__ == "__main__":
    asyncio.run(main())

