import openai
import logging
from config import Config

logger = logging.getLogger("voicebot.speech")
openai.api_key = Config.OPENAI_API_KEY

async def speech_to_text(file_path: str) -> str:
    logger.info("speech-recognized")
    audio_file = open(file_path, "rb")
    transcript = openai.audio.transcribe("whisper-1", audio_file)
    return transcript["text"]