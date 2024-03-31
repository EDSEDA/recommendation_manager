from config import settings
from grifon.video_analysis.schema import VideoAnalyseMessage
from db.utils import session
from db.models import User
import logging


async def get_recommendations(msg: VideoAnalyseMessage):
    """
    1. Получение внутреннего ID пользователя по эмбедингу
    2. Передача ID пользователя с данными из видео анализа в сервис формирования рекомендаций
    """
    logging.info("Start recommendation processing...")

    target_embedding = msg.embedding
    user_id = session.query(User.id).filter(User.embedding == target_embedding).all()


    print(f"Received message: {msg.value().decode('utf-8')} from topic {msg.topic()}")
