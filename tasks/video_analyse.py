from config import settings
from grifon.video_analysis.schema import VideoAnalyseMessage
from grifon.recommendation.schema import CreateUserRecommendationMessage
from db.utils import session
from db.models import User
import logging
from tasks import kafka_client  # Импорт экземпляра KafkaClient
import json


async def _get_recommendations(message: CreateUserRecommendationMessage):
    kafka_client.send_message(settings.RECOMMENDATION_TOPIC, message)
    kafka_client.flush()


@kafka_client.register_topic_handler(settings.VIDEO_ANALYSIS_TOPIC)
async def get_recommendations(msg: VideoAnalyseMessage):
    """
    1. Получение внутреннего ID пользователя по эмбедингу
    2. Передача ID пользователя с данными из видео анализа в сервис формирования рекомендаций
    """
    logging.info("Start recommendation processing...")

    msg = VideoAnalyseMessage.parse_obj(json.loads(msg.value()))
    target_embedding = msg.embedding
    user_id = session.query(User.id).filter(User.embedding == target_embedding).all()

    await _get_recommendations(msg)     # todo: upd message
    logging.info("Sent task to recommendation service")
