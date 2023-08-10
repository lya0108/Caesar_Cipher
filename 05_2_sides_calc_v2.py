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

# does calculations for a, b, c, α, and ß
def sides_2_calc(given_1, length_1, given_2, length_2):
    if given_1 == "b" and given_2 == "c":
        a = round(math.sqrt(length_2**2 - length_1**2), 2)
        b, c = length_1, length_2
    elif given_1 == "a" and given_2 == "c":
        a, c = length_1, length_2
        b = round(math.sqrt(length_2**2 - length_1**2), 2)
    else:
        a, b = length_1, length_2
        c = round(math.sqrt(length_1**2 + length_2**2), 2)
    
    α = math.degrees(math.asin(a/c))
    ß = math.degrees(math.asin(b/c))
    return a, b, c, α, ß

ab = ["a", "b"]
abc = ["a", "b", "c"]

while True:
    while True:
        # asks user for sides info
        given_1 = choice_checker("First Side Given (a / b): ", ab, "Please Enter a / b")
        length_1 = get_int_input(f"Length of Side ({given_1}): ")
        given_2 = choice_checker("\nSecond Side Given (a / b / c): ", abc, "Please Enter a / b / c")

        # checks if both sides are not the same 
        if given_1 == given_2:
            print("I Think You Made A Typo?")
        elif given_1 != given_2:
            length_2 = get_int_input(f"Length of Side ({given_2}): ")
            break
    
    # checks if the hypotenuse is longer than the other side
    if given_2 == "c" and length_2 <= length_1:
        print("Typo?\nYour Hypotenuse Must Be Bigger Than Your Other Side")
        
    else:
        break

a, b, c, α, ß = sides_2_calc(given_1, length_1, given_2, length_2)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"A = {α}")
print(f"B = {ß}")