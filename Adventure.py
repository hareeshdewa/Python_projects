#Choose your own Adventure:

name = input("Type your name: ")
print("Welcome,",name, "to this adventure!!")


while True:
    answer = input("You are on a dirt road, it has come to an end and you can go left or right."
                   " Which way would like to go? ".lower())

    if answer == "left".lower():
        answer = input("You come to a drive, you can walk around it or swim across?"
                       "type walk to walk around and swim to swim across: ")
        if answer == "swim".lower():
            print("You swim across and were eaten by an alligator.")
        elif answer == "walk".lower():
            print("You walk for many miles,ran out of water and you lost the game!")
        else:
            print("Not a valid option.You lose!")
    elif answer == "right".lower():
        answer = input("You come to a bridge, it looks wobbly,"
                       " do you want to cross it or head back? (cross/back)")
        if answer == "cross".lower():
            answer = input("You cross the bridge and meet a stranger. Do you want to "
                           "talk to them (yes or no)? ")
            if answer == "yes".lower():
                print("you talk to the stranger and they give you gold. You win!")
            elif answer == "no".lower():
                print("You ignored the stranger and they are offended and you lose!")
            else:
                print("Not a valid option")
        elif answer == "back".lower():
            print("You got back and lose.")
        else:
            print("Not a valid option, you lose.")

    else:
        print("Not a valid option. You Lose.")

    another_attempt = input("Would you like to try another attempt: ")
    if another_attempt == " Y".lower():
        print("Welcome back")
    elif another_attempt == "N".lower():
        print("Thank You for trying")
        break


print("See you!!")

