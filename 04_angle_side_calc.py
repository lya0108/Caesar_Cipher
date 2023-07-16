import math



angle = input("Angle Given: ")
angle_size = int(input("Angle Size = "))
side_given = input("What Side given (a/b/c): ")
side = int(input("Side Length = "))

sin = math.sin(math.radians(angle_size))
cos = math.cos(math.radians(angle_size))
tan = math.tan(math.radians(angle_size))

if angle == "a" and side_given == "a":
    a = side
    b = side/tan
    c = side/sin
elif angle == "a" and side_given == "b":
    a = side*tan
    b = side
    c = side/cos
elif angle == "a" and side_given == "c":
    a = side*sin
    b = side*cos
    c = side
elif angle == "b" and side_given == "a":
    a = side
    b = side*tan
    c = side/cos
elif angle == "b" and side_given == "b":
    a = side/tan
    b = side
    c = side/sin
elif angle == "b" and side_given == "c":
    a = side*cos
    b = side*sin
    c = side

a = round(a, 2)
b = round(b, 2)
c = round(c, 2)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")