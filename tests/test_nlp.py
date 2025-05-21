import pytest

from nlp import extract_name


@pytest.mark.asyncio
async def test_extract_name():
    text = "My name is Oksana"
    name = await extract_name(text)
    assert name.lower() == "oksana"
