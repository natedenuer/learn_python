a = float(input())
b = float(input())
x = input()
#if x == 0:
    #print("Деление на 0")
if x == ("+"):
    print(a + b)

elif x == ("-"):
    print(a - b)

elif x == ("*"):
    print(a * b)

elif x == ("/"):
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')

elif x == ("*"):
    print(a * b)

elif x == ("mod"):
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')

elif x == ("pow"):
    print(a ** b)

elif x == ("div"):
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')

else: print("нихуя")
