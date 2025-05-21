import logging

logger = logging.getLogger("voicebot.livekit")

class LiveKitClient:
    def __init__(self):
        pass  # тут можна додати реальні параметри, якщо треба

    async def connect(self):
        logger.info("joined-room")
        # For the mock, nothing to do

    async def send_audio(self, file_path: str):
        logger.info(f"tts-sent: {file_path}")
        # Mock: no real sending, just log

    async def receive_audio(self) -> str:
        logger.info("listening audio from user")
        # Mock: just expect 'user_input.wav' in the project folder
        print(">>> Please record user voice as 'user_input.wav' and press Enter to continue...")
        input()
        return "user_input.wav"

    async def disconnect(self):
        logger.info("disconnecting from room")
