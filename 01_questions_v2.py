import math

sides = int(input("How Many Sides Given? "))

if sides >= 2:
    use_pythagoras = input("Do You Need Another Side? ")
    
    if use_pythagoras == "yes":
        find_hypotenuse = input("Do You Need The Hypotenuse? ")

        if find_hypotenuse == "yes":
            a = int(input("a = "))
            b = int(input("b = "))
            c = math.sqrt(a*a + b*b)
            print(f"hypotenuse = {c}")
        
        else:
            c = int(input("c = "))
            b = int(input("b = "))
            a = math.sqrt(c*c - b*b)
            print(f"3rd Side = {a}")

    else:
        print("Leave Empty If Not Used")
        a = int(input("a = "))
        o = int(input("o = "))
        h = int(input("h = "))
        
        if a == "":
            angle = math.asin(o/h)
        elif o == "":
            angle = math.acos(a/h)
        else:
            angle = math.atan(o/a)

else:
    print("You Should Have 1 Side And 1 Angle")
    side = int(input("Side Length = "))
    angle = int(input("Angle = "))
    side_to_find = input("What Side given (a/o/h): ")

    if side_to_find == "a":
        angle = math.sin()



