from config import settings
from grifon.video_analysis.schema import VideoAnalyseMessage


async def get_recommendations(msg: VideoAnalyseMessage):
    """Пример обработчика сообщения."""
    print(f"Received message: {msg.value().decode('utf-8')} from topic {msg.topic()}")


