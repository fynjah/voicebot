import logging
from typing import Optional

import openai

from config import Config

logger = logging.getLogger("voicebot.nlp")
openai.api_key = Config.OPENAI_API_KEY


async def extract_name(text: str) -> Optional[str]:
    logger.info("name-detected")
    prompt = (
        "Extract the person's first name from this text: "
        f'"{text}"\n'
        "Reply with the name only, no explanations."
    )
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You help extract a person's "
                "first name from a conversation.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=10,
    )
    name = response.choices[0].message.content.strip()
    if not name or len(name.split()) > 2 or len(name) > 30:
        return None
    return name
