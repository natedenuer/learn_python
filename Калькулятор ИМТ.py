weight = int(input())
height = float(input())

index = weight / height ** 2

if index < 18.5:
    print("Underweight")

elif (18.5 <= index < 25):
    print("Normal")

elif (25 <= index < 30):
    print("Overweight")

else:
    print("Obesity")

