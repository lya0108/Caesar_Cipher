
# checks input is a number and is bigger than 0
def get_int_input(question, error):
    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response
        
            else:
                print(error)
        
        except ValueError:
            print(error)

while True:
    prompt = get_int_input("Input: ", "Please Enter a Number Bigger Than 0")
    print("Program Continues")
