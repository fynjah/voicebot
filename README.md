# VoiceBot

**Minimal real-time voice bot** using LiveKit, OpenAI STT/TTS, LangChain for name extraction.

## Features
- Connects to a LiveKit room as "VoiceBot"
- Greets the user: "Hello! What is your name?"
- Recognizes speech (OpenAI Whisper), extracts name (LangChain/OpenAI)
- Responds: "Nice to meet you, <Name>!"
- Modular, type-annotated, with logging and tests

## Run locally

1. Create `.env` (see `.env.example`)
2. `docker-compose up --build`

## Project Structure

- `main.py` — entrypoint
- `livekit_client.py` — LiveKit integration
- `speech.py` — Speech-to-text (OpenAI)
- `tts.py` — Text-to-speech (OpenAI)
- `nlp.py` — Name extraction (LangChain/OpenAI)
- `logic.py` — Orchestration
- `tests/` — Unit tests

## Testing

- Unit tests for NLP and reply logic (`pytest`)
- Integration tests: mock LiveKit/STT/TTS components

## Diagram

```mermaid
sequenceDiagram
  participant User
  participant Bot
  participant OpenAI
  participant LiveKit

  Bot->>LiveKit: join room
  Bot->>User: play "Hello! What is your name?"
  User->>Bot: says name (audio)
  Bot->>OpenAI: speech-to-text
  OpenAI->>Bot: returns text
  Bot->>OpenAI: extract name (LangChain/Prompt)
  OpenAI->>Bot: returns name
  Bot->>User: play "Nice to meet you, <Name>!"
