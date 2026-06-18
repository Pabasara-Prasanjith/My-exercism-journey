"""collatz conjecture step calculator"""
def steps(number):
    step_counter = 0
    if number <= 0:
        """example when argument is zero or a negative integer"""
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        step_counter += 1
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
    return step_counter