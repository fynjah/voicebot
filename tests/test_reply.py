def build_reply(name: str) -> str:
    if name:
        return f"Nice to meet you, {name}!"
    else:
        return "Sorry, I didn't catch your name. Please try again!"

def test_build_reply():
    assert build_reply("Oksana") == "Nice to meet you, Oksana!"
    assert build_reply("") == "Sorry, I didn't catch your name. Please try again!"
