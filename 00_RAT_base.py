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
def get_int_input(question, mode):
    while True:
        
        response = (input(question))

        if mode == "":

            try:
                response = float(response)

                if response > 0:
                    return response

                else:
                    print("Please Enter A Number Bigger Than 0")
            
            except ValueError:
                print("Please Enter A Number Bigger Than 0")
        
        elif mode == "angle":

            try:
                response = float(response)

                if 0 < response < 90:
                    return response

                else:
                    print("Please Enter A Number Between 0 And 90")
            
            except ValueError:
                print("Please Enter A Number Between 0 And 90")
        
        else: 
            try:
                response = int(response)

                if response > 0:
                    return response

                else:
                    print("Please Enter A Whole Number Bigger Than 0")
            
            except ValueError:
                print("Please Enter A Whole Number Bigger Than 0")
            
# does calculations when given 1 side and 1 angle 
def angle_side_calc():

    print("You Should Have An Angle and A Side\n")

    # asks user for angle and side info
    angle = choice_checker("What Angle Given A(α) / B(ß): ", ab, "Please Enter A / B")
    angle_size = get_int_input("Size of Angle = ", "angle")
    side_given = choice_checker("\nWhat Side given (a / b / c): ", abc, "Please Enter a / b / c")
    side = get_int_input("Side Length = ", "")
    
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
        angle = "α"
        α = round(angle_size, 2)
        ß = 90 - α
    else:
        angle = "ß"
        ß = round(angle_size, 2)
        α = 90 - ß
        
    question = (f"{angle}={angle_size}°,{side_given}={side}")

    question_list.append(question)
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    α_list.append(α)
    ß_list.append(ß)

# does calculations when given 2 sides
def sides_2_calc():
    print("\n")
    while True:
        while True:
            # asks user for sides info
            given_1 = choice_checker("First Side Given (a / b): ", ab, "Please Enter a / b")
            length_1 = get_int_input(f"Length of Side ({given_1}): ", "")
            given_2 = choice_checker("\nSecond Side Given (a / b / c): ", abc, "Please Enter a / b / c")

            if given_1 == given_2:
                print("I Think You Made A Typo?")
            elif given_1 != given_2:
                length_2 = get_int_input(f"Length of Side ({given_2}): ", "")
                break
        
        if given_2 == "c" and length_2 <= length_1:
            print("Typo?\nYour Hypotenuse Must Be Bigger Than Your Other Side")
            
        else:
            break

    # calculations
    if given_1 == "b" and given_2 == "c":
        a = round(math.sqrt(length_2**2 - length_1**2), 2)
        b = length_1
        c = length_2
        α = math.acos(length_1/length_2)
        ß = math.asin(length_1/length_2)
    elif given_1 == "a" and given_2 == "c":
        a = length_1
        b = round(math.sqrt(length_2**2 - length_1**2), 2)
        c = length_2
        α = math.asin(length_1/length_2)
        ß = math.acos(length_1/length_2)
    elif given_1 == "a" and given_2 == "b":
        a = length_1
        b = length_2
        c = round(math.sqrt(length_1**2 + length_2**2), 2)
        α = math.atan(length_1/length_2)
        ß = math.atan(length_2/length_1)
    else:
        a = length_2
        b = length_1
        c = round(math.sqrt(length_1**2 + length_2**2), 2)
        α = math.atan(length_2/length_1)
        ß = math.atan(length_1/length_2)
    
    α = math.degrees(α)
    ß = math.degrees(ß)

    a = round(a, 2)
    b = round(b, 2)
    c = round(c, 2)
    α = round(α, 2)
    ß = round(ß, 2)

    question = (f"{given_1}={length_1},{given_2}={length_2}")

    question_list.append(question)
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    α_list.append(α)
    ß_list.append(ß)

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
α_list = []
ß_list = []

# dictionary
variable_dict = {
    "Given": question_list,
    "a": a_list,
    "b": b_list,
    "c": c_list,
    "α": α_list,
    "ß": ß_list,
}

# main routine
# color (personal preference)
print("\x1b[38;2;0;255;255m")

# asks if user wants instructions
instructions = choice_checker("Do You Want The Instructions (Recommended): ", yesno, "Please Enter Yes or No")
if instructions == "yes":
    print("Side (c) = Hypotenuse\nSide (a/b) = Other Sides of Triangle\nAngle A(α) = Opposite of Side (a)\nAngle B(ß) = Opposite of Side (b)\n")
    print("""
                ß
               /|
              / |
             /  |
            /   |
        c  /    | a
          /     |
         /      |
        /       |
       /        |
    α /_________| 
           b
    """)
    print("*For Reference*\nPlease Note: All Units Must Be The Same For Answers To Be Relevant♥\nAnd All Values Are Rounded To 2 Decimal Places\n")
# asks user for number of questions
while True:
    num_questions = get_int_input("How Many Questions: ", "♥")

    if num_questions <= 100:
        break
    
    else:
        print(f"You Really Gonna Do {num_questions} Questions!?!?!?!?\nOr Was That A Typo?")

current_question = 1

while num_questions >= current_question:

    # heading for each question
    heading = f"\n==== Question {current_question} of {num_questions} ====\n"
    print(heading)

    sides = choice_checker("How Many Sides Given 1 Or 2? (Type xxx to Exit) ", onetwo, "Please Enter 1 or 2, or xxx to Exit")

    if sides == "2":
        # find angle size (using 2 sides)  --- complete
        sides_2_calc()

    # exit code
    elif sides == "xxx":
        break

    # find a side using an angle and side  --- complete
    else:
        angle_side_calc()
    
    current_question = current_question + 1

info_frame = pandas.DataFrame(variable_dict)
info_frame = info_frame.set_index("Given")

# currency Formatting
add_degree = ["α", "ß"]
for item in add_degree:
    info_frame[item] = info_frame[item].apply(degree_symbol)

if info_frame.empty:
    print("\n==== No Questions Asked ====")
else:
    print(info_frame)
    print("\n!!!!!All Values Are ROUNDED to 2 Decimal Places!!!!!")