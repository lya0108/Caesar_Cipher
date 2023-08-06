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
sin = math.sin(math.radians(angle_size))
cos = math.cos(math.radians(angle_size))
tan = math.tan(math.radians(angle_size))

# calculates a, b, c, A, and B then appends it
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