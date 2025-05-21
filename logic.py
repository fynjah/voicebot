import logging
from livekit_client import LiveKitClient
from speech import speech_to_text
from tts import text_to_speech
from nlp import extract_name

logger = logging.getLogger("voicebot.logic")

async def main_logic():
    lk = LiveKitClient()
    await lk.connect()

    greeting = "Hello! What is your name?"
    await text_to_speech(greeting, "greeting.wav")
    await lk.send_audio("greeting.wav")

    audio_file = await lk.receive_audio()
    user_text = await speech_to_text(audio_file)
    logger.info(f"speech recognized: {user_text}")

    name = await extract_name(user_text)
    logger.info(f"Detected name: {name}")

    if name:
        reply = f"Nice to meet you, {name}!"
    else:
        reply = "Sorry, I didn't catch your name. Please try again!"

    await text_to_speech(reply, "reply.wav")
    await lk.send_audio("reply.wav")

    await lk.disconnect()
