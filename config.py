from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    LIVEKIT_URL = os.getenv("LIVEKIT_URL")
    LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
    LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ROOM_NAME = os.getenv("ROOM_NAME", "VoiceBot")
    BOT_IDENTITY = os.getenv("BOT_IDENTITY", "VoiceBot")
