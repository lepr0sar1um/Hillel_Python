import random
from math import sqrt


def find_square(a, b, c):
    return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0


def generate_random_triangle():
    x1y1 = (random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))
    x2y2 = (random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))
    x3y3 = (random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))

    s = find_square(x1y1, x2y2, x3y3)
    if s < 0.0001:
        generate_random_triangle()

    print(f"A{x1y1}, B{x2y2}, C{x3y3} S = {s}")


def create_right_triangle(x1y1):
    x2 = x1y1[0] + (10 * sqrt(2))
    y3 = x1y1[1] + (10 * sqrt(2))

    x2y2 = (x2, x1y1[1])
    x3y3 = (x1y1[0], y3)
    s = find_square(x1y1, x2y2, x3y3)
    print(f"A{x1y1}, B{x2y2}, C{x3y3} S = {s}")


a = (random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))
create_right_triangle(a)
generate_random_triangle()
