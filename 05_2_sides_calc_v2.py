import math

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

ab = ["a", "b"]
abc = ["a", "b", "c"]

# asks user for sides info
given_1 = choice_checker("First Side Given (a / b): ", ab, "Please Enter a / b")
length_1 = get_int_input(f"Length of Side ({given_1}): ")
given_2 = choice_checker("Second Side Given (a / b / c): ", abc, "Please Enter a / b / c")

if given_1 == given_2:
    print("I Think You Made A Typo?")
else:
    length_2 = get_int_input(f"Length of Side ({given_2}): ")

# calculations
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

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"A = {cap_A}")
print(f"B = {cap_B}")