def is_pangram(sentence):
    the_list = {
        "a": False, 'b': False, 'c': False, 'd': False, 'e': False, 'f': False,
        'g': False, 'h': False, 'i': False, 'j': False, 'k': False, 'l': False,
        'm': False, 'n': False, 'o': False, 'p': False, 'q': False, 'r': False,
        's': False, 't': False, 'u': False, 'v': False, 'w': False, 'x': False,
        'y': False, 'z': False
    }
    sentence = sentence.lower().strip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in sentence:
        if char in alphabet:
            the_list[char] = True

    return all(the_list.values())
