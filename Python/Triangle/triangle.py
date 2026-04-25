def is_triangle(sides):
    a, b, c = sides
    return min(sides) > 0 and (a + b >= c and a + c >= b and b + c >= a)
    
def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    a, b, c = sides
    return is_triangle(sides) and (a == b or a == c or b == c)

def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3
