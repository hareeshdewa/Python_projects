def continue_method(func):
    def wrapper():
        second_attempt = True
        while second_attempt:
            second_attempt = input("Press Y to Start, or Press N to quite: ").lower()
            if second_attempt == "N".lower():
                print("Byee.....")
                quit()
            func()
    return wrapper

@continue_method
def calculator():
    print("Welcome!!!!!")
    print("To add, Press 1", "\n"
          "To sub, Press 2", "\n"
          "To Multiple, Press 3", "\n"
          "To Divide, Press 4", "\n")

    user = True
    while user:
        try:
            user = eval(input("Enter the operator to continue: "))
            if user < 1 or user > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
            else:
                break
        except ValueError and NameError:
            print("Invalid input. Please enter a valid number.")

    first_number = input("Enter the first Number: ")
    second_number = input("Enter the second Number: ")

    if not first_number.isdigit() and not second_number.isdigit():
        print("Invalid format.....")
        quit()
    else:
        first_number = eval(first_number)
        second_number = eval(second_number)

    if user == 1:
        add = Addition(first_number,second_number)
        print(add)
    elif user == 2:
        sub = Sutraction(first_number,second_number)
        print(sub)
    elif user == 3:
        multiply = Multiplication(first_number,second_number)
        print(multiply)
    else:
        if user == 4:
            try:
                division = Division(first_number,second_number)
                print(division)
            except ZeroDivisionError:
                print("Invalid Format")

def Addition(num1,num2):
    return num1 + num2

def Sutraction(num1,num2):
    return num1 - num2

def Multiplication(num1,num2):
    return num1 * num2

def Division(num1, num2):
    return num1 / num2

calculator()