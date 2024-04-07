from config import settings
from grifon.video_analysis.schema import VideoAnalyseMessage
from grifon.recommendation.schema import CreateUserRecommendationMessage, UserRecommendationMessage
# from db.utils import session
# from db.models import User
import logging
from tasks import kafka_client


async def _get_recommendations(message: CreateUserRecommendationMessage):
    kafka_client.send_message(settings.RECOMMENDATION_TOPIC, message)
    kafka_client.flush()


@kafka_client.register_topic_handler(settings.VIDEO_ANALYSIS_TOPIC, msg_class=VideoAnalyseMessage)
async def get_recommendations_from_video(msg: VideoAnalyseMessage):
    """
    1. Получение внутреннего ID пользователя по эмбедингу
    2. Передача ID пользователя с данными из видео анализа в сервис формирования рекомендаций
    """
    logging.info("Start recommendation processing...")

    # target_embedding = msg.embedding
    # user_id = session.query(User.id).filter(User.embedding == target_embedding).all()

    get_rec_msg = CreateUserRecommendationMessage.parse_obj(dict(msg) | dict(user_id=1))
    await _get_recommendations(get_rec_msg)
    logging.info("Sent task to recommendation service")


@kafka_client.register_topic_handler(settings.RECOMMENDATION_RESPONSE_TOPIC, msg_class=UserRecommendationMessage)
async def get_recommendations_from_rec_service(msg: UserRecommendationMessage):
    """
    1. Рекомендации получены от сервиса рекомендаций
    """
    logging.info(f"Recommendation for {msg.user_id} is: {msg.recommendations}")
    return

