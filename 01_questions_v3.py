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


yesno = ["yes", "no"]
onetwo = ["1", "2"]

sides = choice_checker("How Many Sides Given (1 Or 2)? ", onetwo, "Please Enter 1 or 2")

if sides == "2":
    use_pythagoras = choice_checker("Do You Need Another Side? ", yesno, "Please Enter Yes or No")
    
    if use_pythagoras == "yes":
        find_hypotenuse = choice_checker("Do You Need The Hypotenuse? ", yesno, "Please Enter Yes or No")

        if find_hypotenuse == "yes":
            base = get_int_input("Base = ")
            height = get_int_input("Height = ")
            hypotenuse = round(math.sqrt(base**2 + height**2), 2)
            print(f"hypotenuse = {hypotenuse}")
        
        else:
            hypotenuse = get_int_input("Hypotenuse = ")
            height = get_int_input("Height = ")
            base = math.sqrt(hypotenuse**2 - height**2)
            print(f"Base = {base}")

    else:
        print("Leave Empty If Not Used")
        a = get_int_input("a = ")
        o = get_int_input("o = ")
        h = get_int_input("h = ")
        
        if a == "":
            angle = math.asin(o/h)
        elif o == "":
            angle = math.acos(a/h)
        else:
            angle = math.atan(o/a)

else:
    print("You Should Have 1 Side And 1 Angle")
    side = get_int_input("Side Length = ")
    side_to_find = input("What Side given (a/o/h): ")
    angle = get_int_input("Angle = ")

    if side_to_find == "a":
        angle = math.sin()