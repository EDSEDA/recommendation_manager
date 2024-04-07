import json

from config import settings
from grifon.video_analysis.schema import VideoAnalysisMessage
from grifon.recommendation.schema import CreateUserRecommendationMessage, UserRecommendationMessage
# from db.utils import session
# from db.models import User
import logging
from tasks import kafka_client  # Импорт экземпляра KafkaClient


async def _request_recommendations(message: CreateUserRecommendationMessage):
    kafka_client.send_message(settings.RECOMMENDATION_REQUEST_TOPIC, message)
    kafka_client.flush()


@kafka_client.register_topic_handler(settings.VIDEO_ANALYSIS_TOPIC)
async def get_video_data(msg: VideoAnalysisMessage):
    """
    1. Получение внутреннего ID пользователя по эмбедингу
    2. Передача ID пользователя с данными из видео анализа в сервис формирования рекомендаций
    """
    logging.info("Start recommendation processing...")
    msg = CreateUserRecommendationMessage.parse_obj(json.loads(msg.value()) | dict(user_id=3))

    await _request_recommendations(msg)     # todo: upd message
    logging.info("Sent task to recommendation service")


@kafka_client.register_topic_handler(settings.RECOMMENDATION_RESPONSE_TOPIC)
async def get_recommendations(msg: UserRecommendationMessage):

    logging.info("Start recommendation processing...")
    msg = UserRecommendationMessage.parse_obj(json.loads(msg.value()))

    logging.info(msg)
