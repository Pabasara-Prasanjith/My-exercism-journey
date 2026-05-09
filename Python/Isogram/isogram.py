def is_isogram(string):
    string = string.replace(" ", "")
    string = string.replace("-", "")
    string = string.lower()
    
    seen = set()
    duplicates = set()

    for char in string:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    
    if duplicates == set():
        return True
    else:
        return False

tests = ["", "isogram", "eleven", "zzyzx", "subdermatoglyphic", "Alphabet", "alphAbet", "thumbscrew-japingly", "thumbscrew-jappingly", "six-year-old", "Emily Jung Schwartzkopf", "accentor", "angola", "up-to-date"]
for test in tests:
    print(is_isogram(test))
