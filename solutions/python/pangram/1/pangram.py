def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower().strip()
    for char in sentence:
        if char in alphabet:
            alphabet = alphabet.replace(char, "")

    return alphabet == ""
