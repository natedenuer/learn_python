a = int(input())
b = int(input())
c = int(input())

if (c<=b<=a):
    max = a
    min = c
    print (max)
    print(min)
    print(b)
elif (a<=b<=c):
    max = c
    min = a
    print(max)
    print(min)
    print(b)
elif (b <= c <= a):
    max = a
    min = b
    print(max)
    print(min)
    print(c)
elif (a <= c <= b):
    max = b
    min = a
    print(max)
    print(min)
    print(c)
elif (b <= a <= c):
    max = c
    min = b
    print(max)
    print(min)
    print(a)
elif (c <= a <= b):
    max = b
    min = c
    print(max)
    print(min)
    print(a)
else:
    print("xyq")