def response(hey_bob):
    respond = "Whatever."
    strip_text = hey_bob.strip()
    if strip_text.endswith("?"):
        respond = "Sure."
    if hey_bob.isupper():
        respond = "Whoa, chill out!"
    if hey_bob.endswith("?") and hey_bob.isupper():
        respond = "Calm down, I know what I'm doing!"
    if not strip_text:
        respond = "Fine. Be that way!"
    return respond
