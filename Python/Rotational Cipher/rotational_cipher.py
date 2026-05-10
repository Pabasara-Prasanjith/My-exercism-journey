def rotate(text, key):
    output = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                new_char = chr(65 + ((ord(char) - 65 + key) % 26))
                output += new_char
            elif char.islower():
                new_char = chr(97 + ((ord(char) - 97 + key) % 26))
                output += new_char
        else:
            output += char
    return output

print(rotate("pajdhgydb? hfh  hyh.", 226))
