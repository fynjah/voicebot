import logging

import openai

logger = logging.getLogger("voicebot.tts")


async def text_to_speech(text: str, output_path: str):
    client = openai.OpenAI()
    response = client.audio.speech.create(
        model="tts-1", input=text, voice="alloy"
    )
    with open(output_path, "wb") as f:
        f.write(response.content)
    logger.info("tts-sent")
