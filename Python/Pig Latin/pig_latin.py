vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def translate(text):
    global vowels
    text_tuple = text.split()
    output_words = []
    for text in text_tuple:
        output_text = ""
        # test 2 done
        for char in text:
            if char in vowels and char != text[0]:
                split_no_0 = text.split(char, 1)[0]
                split_no_1 = text.split(char, 1)[1]
                print(split_no_0)
                print(split_no_1)
                output_text = char + split_no_1 + split_no_0 + "ay"
                break

        # test 4 done
        if "y" in text and text[0] != "y":
            split_no_0 = text.split("y", 1)[0]
            char_replace_answer = True
            for char in split_no_0:
                if char in vowels:
                    char_replace_answer = True
                    break
                else:
                    char_replace_answer = False
            if not char_replace_answer:
                split_no_1 = text.split("y", 1)[1]
                output_text = "y" + split_no_1 + split_no_0 + "ay"

        # test 3 done
        if text.startswith("qu"):
            split_no_0 = text.split("u", 1)[1]
            output_text = split_no_0 + "qu" + "ay"
        elif "qu" in text and not text.startswith("qu"):
            split_no_0 = text.split("u", 1)[0]
            char_split_answer = True
            for char_split in split_no_0:
                if char_split in vowels:
                    char_split_answer = True
                    break
                else:
                    char_split_answer = False
            if not char_split_answer:
                split_no_1 = text.split("u", 1)[1]
                output_text = split_no_1 + split_no_0 + "uay"

        # test 1 done
        for sw_compare in ["xr", "yt"]:
            if sw_compare == text[:2] or text[0] in vowels:
                output_text = text + "ay"
                break

        output_words += [output_text]
    output_string = " ".join(output_words)
    return output_string
