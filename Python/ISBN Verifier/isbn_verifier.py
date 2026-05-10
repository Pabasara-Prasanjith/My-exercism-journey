def is_valid(isbn):
    valid_isbn = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]
    isbn = isbn.replace("-" ,"")
    if len(isbn) == 10:
        count = 0
        multiplier = 10
        output = 0
        for num in isbn:
            if count != 10 and num in valid_isbn and num != "X":
                output += int(num) * multiplier
                multiplier -= 1
                count += 1
            elif count == 9 and num in valid_isbn:
                if num == "X":
                    output += 10 * multiplier
                    count += 1
                else:
                    output += int(num) * multiplier
                    count += 1
            else:
                return False

        if count == 10:
            return output % 11 == 0
    else:
        return False

tests = ["3-598-21508-8", "3-598-21508-9", "3-598-21507-X", "3-598-21507-A", "4-598-21507-B", "3-598-P1581-X", "3-598-2X507-9", "3-598-21508-96", "3-598-2X507-5", "3598215088", "359821507X", "359821507", "3598215078X", "00", "3-598-21507", "3-598-21515-X", "", "134456729", "3132P34035", "3598P215088", "98245726788"]

for test in tests:
    print(is_valid(test))
