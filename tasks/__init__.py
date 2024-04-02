from config import settings
from grifon.mqbroker.kafka_client import KafkaClient

kafka_client = KafkaClient(f"localhost:{settings.KAFKA_CLIENT_PORT}")


async def start_handling():
    await kafka_client.start_handling()

