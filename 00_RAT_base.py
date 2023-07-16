import math
import pandas

# checks that choice is within choosen list
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

# checks input is a number and is bigger than 0
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

# does calculations when given 1 side and 1 angle 
def angle_side_calc():

    print("You Should Have An Angle and A Side")
    angle = choice_checker("What Angle Given (A / B): ", ab, "Please Enter A / B")
    angle_size = get_int_input("Angle Size = ")
    side_given = choice_checker("What Side given (a / b / c):\n", abc, "Please Enter a / b / c")
    side = get_int_input("Side Length = ")
    
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

    if angle == "a":
        cap_A = angle_size
        cap_B = 90 - angle_size
    else:
        cap_A = 90 - angle_size
        cap_B = angle_size
    
    question = (f"{angle.upper} = {angle_size}, {side_given} = {side}")

    question_list.append(question)
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    cap_A_list.append(cap_A)
    cap_B_list.append(cap_B)

# does calculations when given 2 sides
def sides_2_calc():
    while True:
        given_1 = choice_checker("First Side Given (a / b): ", ab, "Please Enter a / b")
        length_1 = get_int_input(f"Length of Side ({given_1}): ")
        given_2 = choice_checker("Second Side Given (a / b / c): ", abc, "Please Enter a / b / c")

        if given_1 == given_2:
            print("I Think You Made A Typo?")
        else:
            length_2 = get_int_input(f"Length of Side ({given_2}): ")
            break

    if given_1 == "b" and given_2 == "c":
        a = round(math.sqrt(length_2**2 - length_1**2), 2)
        b = length_1
        c = length_2
        cap_A = math.acos(length_1/length_2)
        cap_B = math.asin(length_1/length_2)
    elif given_1 == "a" and given_2 == "c":
        a = length_1
        b = round(math.sqrt(length_2**2 - length_1**2), 2)
        c = length_2
        cap_A = math.asin(length_1/length_2)
        cap_B = math.acos(length_1/length_2)
    elif given_1 == "a" and given_2 == "b":
        a = length_1
        b = length_2
        c = round(math.sqrt(length_1**2 + length_2**2), 2)
        cap_A = math.atan(length_1/length_2)
        cap_B = math.atan(length_2/length_1)
    else:
        a = length_2
        b = length_1
        c = round(math.sqrt(length_1**2 + length_2**2), 2)
        cap_A = math.atan(length_2/length_1)
        cap_B = math.atan(length_1/length_2)
    
    cap_A = math.degrees(cap_A)
    cap_B = math.degrees(cap_B)

    question = (f"{given_1} = {length_1}, {given_2} = {length_2}")

    question_list.append(question)
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    cap_A_list.append(cap_A)
    cap_B_list.append(cap_B)

# applies degree sign
def degree_symbol(x):
    # adds ° to the back
    return "{}°".format(x)

yesno = ["yes", "no"]
onetwo = ["1", "2", "xxx"]
ab = ["a", "b"]
abc = ["a", "b", "c"]

# list of variables 
question_list = []
a_list = []
b_list = []
c_list = []
cap_A_list = []
cap_B_list = []

# dictionary
variable_dict =                                                                                                                                {
    "Given": question_list,
    "a": a_list,
    "b": b_list,
    "c": c_list,
    "A": cap_A_list,
    "B": cap_B_list,
}

# main routine
# color (personal preference)
print("\x1b[38;2;0;255;255m")

# asks if user wants instructions
instructions = choice_checker("Do You Want The Instructions (Recommended): ", yesno, "Please Enter Yes or No")
if instructions == "yes":
    print("Side (c) = Hypotenuse\nSide (a/b) = Other Sides of Triangle\nAngle (A) = Opposite of Side (a)\nAngle (B) = Opposite of Side (b)\n")
    print("""
                B
               /|
              / |
             /  |
            /   |
        c  /    | a
          /     |
         /      |
        /       |
       /        |
    A /_________| 
           b
    """)
    print("*For Reference*\n")

num_questions = round(get_int_input("How Many Questions: "))
current_question = 1

while num_questions >= current_question:

    # heading for each question
    heading = f"\nQuestion {current_question} of {num_questions}\n"
    print(heading)

    sides = choice_checker("How Many Sides Given (1 Or 2)? ", onetwo, "Please Enter 1 or 2, or xxx to exit")

    if sides == "2":
        use_pythagoras = choice_checker("Do You Need Another Side? ", yesno, "Please Enter Yes or No")
        
        if use_pythagoras == "yes":
            find_hypotenuse = choice_checker("Do You Need The Hypotenuse? ", yesno, "Please Enter Yes or No")
            
            # finds hypotenuse (using 2 sides) --- complete
            if find_hypotenuse == "yes":
                a = get_int_input("a = ")
                b = get_int_input("b = ")
                c = round(math.sqrt(a**2 + b**2), 2)
                cap_A = round(math.degrees(math.atan(a/b)), 2)
                cap_B = round(math.degrees(math.atan(b/a)), 2)
                question = f"a = {a}, b = {b}"
            
            # finds another side (using 2 sides) --- complete
            else:
                c = get_int_input("c = ")
                b = get_int_input("b = ")
                a = round(math.sqrt(c**2 - b**2), 2)
                cap_A = round(math.degrees(math.atan(a/b)), 2)
                cap_B = round(math.degrees(math.atan(b/a)), 2)
                question = f"c = {c}, b = {b}"

            question_list.append(question)
            a_list.append(a)
            b_list.append(b)
            c_list.append(c)
            cap_A_list.append(cap_A)
            cap_B_list.append(cap_B)

        # find angle size (using 2 sides)  --- complete
        else:
            sides_2_calc()

    elif sides == "xxx":
        break

    # find a side using an angle and side  --- complete
    else:
        angle_side_calc()
    
    current_question = current_question + 1

info_frame = pandas.DataFrame(variable_dict)
info_frame = info_frame.set_index("Given")

# currency Formatting
add_degree = ["A", "B"]
for item in add_degree:
    info_frame[item] = info_frame[item].apply(degree_symbol)

print(info_frame)