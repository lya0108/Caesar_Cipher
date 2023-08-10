import math

def choice_checker(question, valid_list, error):

    while True:
        
        # asks user for choice
        response = input(question).lower()

        # checks if input is in list
        for item in valid_list:
            if response == item[:1] or response == item:
                return item
        
        print(error)
        print()

def get_int_input(question):
    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response
        
            else:
                print("Please Enter A Number Bigger Than 0")
        
        except ValueError:
            print("Please Enter A Number Bigger Than 0")

ab = ["a", "b"]
abc = ["a", "b", "c"]

angle = choice_checker("What Angle Given (A / B): ", ab, "Please Enter A / B")
angle_size = get_int_input("Size of Angle = ")
side_given = choice_checker("What Side given (a / b / c):\n", abc, "Please Enter a / b / c")
side = get_int_input("Side Length = ")

# converts angle from radians to degrees
angle_degrees = math.radians(angle_size)
sin = math.sin(angle_degrees)
cos = math.cos(angle_degrees)
tan = math.tan(angle_degrees)

# Calculates a, b, c, A, and B
side_values = {
    ("a", "a"): (side, side / tan, side / sin),
    ("a", "b"): (side * tan, side, side / cos),
    ("a", "c"): (side * sin, side * cos, side),
    ("b", "a"): (side, side * tan, side / cos),
    ("b", "b"): (side / tan, side, side / sin),
    ("b", "c"): (side * cos, side * sin, side),
}

a, b, c = side_values[(angle, side_given)]

a = round(a, 2)
b = round(b, 2)
c = round(c, 2)

if angle == "a":
    cap_A = angle_size
    cap_B = 90 - angle_size
else:
    cap_A = 90 - angle_size
    cap_B = angle_size

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"A = {cap_A}")
print(f"B = {cap_B}")