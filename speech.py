import openai
import logging

logger = logging.getLogger("voicebot.speech")


async def speech_to_text(file_path: str) -> str:
    logger.info("speech-recognized")
    audio_file = open(file_path, "rb")
    client = openai.OpenAI()
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcript.text
