"""Find armstrong numbers"""
def is_armstrong_number(number):
    """You can find if a number is an armstrong number"""
    num_as_str = str(number) 
    num_length = len(num_as_str)
    total = 0
    for digit in num_as_str:
        total += int(digit) ** num_length
    return number == total
