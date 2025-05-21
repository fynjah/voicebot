import openai
import logging
from config import Config

logger = logging.getLogger("voicebot.tts")
openai.api_key = Config.OPENAI_API_KEY

async def text_to_speech(text: str, output_path: str):
    response = openai.audio.speech.create(
        model="tts-1",
        input=text,
        voice="alloy"
    )
    with open(output_path, "wb") as f:
        f.write(response.content)
    logger.info("tts-sent")