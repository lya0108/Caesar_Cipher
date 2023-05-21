import math

# takes input and checks if input is a integer that is bigger than 0
def get_int_input(question, error):
    while True:
        try:
            response = int(input(question))
        
        except ValueError:
            print(error)
        
        if response > 0:
            return response
            
        else:
            print(error)

base = get_int_input("Base: ", "Please Enter a Number Bigger Than 0")
height = get_int_input("Height: ", "Please Enter a Number Bigger Than 0")
decimal_places = int(input("How Many Decimal Places: "))
hypotenuse = math.sqrt(base**2 + height**2)
print(f"{hypotenuse:2f}")