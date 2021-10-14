a = int(input())
b = int(input())

def evklid(a, b): # Функція знаходження найбільшого спільного дільника
    if a % b == 0:
        return b
    else:
        return evklid(b, a%b)

#print (evklid(a, b))

nsk = a * b // evklid(a, b) # Знаходимо найменше спільне кратне
print(nsk)
