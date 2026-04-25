"""Raindrops Exercise"""
def convert(number):
    """This is the main function"""
    raindrop_output = ""
    if number % 3 == 0:
        raindrop_output += "Pling"
    if number % 5 == 0:
        raindrop_output += "Plang"
    if number % 7 == 0:
        raindrop_output += "Plong"
    if not raindrop_output:
        raindrop_output = str(number)
    return raindrop_output
