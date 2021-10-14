import math
start = input()

if start == ("треугольник"):
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2

    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
elif start == ("прямоугольник"):
    a = int(input())
    b = int(input())

    s = a * b
    print(s)

elif start == ("круг"):
    r = int(input())
    s = 3.14 * r**2
    print(s)