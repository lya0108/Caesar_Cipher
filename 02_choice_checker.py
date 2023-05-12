
# checks that choice is within choosen list
def choice_checker(question, valid_list, error, num_letters):

    while True:
        
        # asks user for choice
        response = input(question).lower()

        # checks if input is in list
        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item
        
        print(error)
        print()

yesno = ["yes", "no"]
onetwo = [1, 2]

yes_or_no = choice_checker("Yes Or No", yesno, "Please Enter Yes Or No", 1)
one_or_two = choice_checker("1 Or 2", onetwo, "Please Enter 1 Or 2", 1)
print(yes_or_no)
print(one_or_two)