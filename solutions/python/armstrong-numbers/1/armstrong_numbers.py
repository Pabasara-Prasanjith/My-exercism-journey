def is_armstrong_number(number):
    num_as_str = str(number) 
    num_length = len(num_as_str)
    store_num = []
    for digit in num_as_str:
        digit = int(digit)
        num_raise = digit ** num_length
        store_num.append(num_raise)
    return number == sum(store_num)