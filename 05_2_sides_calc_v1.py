import math

given_1 = input("First Side Given (A Or O): ")
given_2 = input("Second Side Given (A / O / H): ")
a = 1
b = 2

if given_1 == "a" and given_2 == "h":
    angle = math.acos(a/b)
elif given_1 == "o" and given_2 == "h":
    angle = math.asin(given_1/given_2)
elif given_1 == "a" and given_2 == "o":
    angle = math.atan(given_2/given_1)
else:
    angle = math.atan(given_1/given_2)

print(math.degrees(angle))