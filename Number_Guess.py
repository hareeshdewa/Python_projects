import random

def number_guess():
    number_range = input("Type a number: ")
    if number_range.isdigit():
        number_range = int(number_range)

        if number_range <= 0:
            print("Enter the number that is larger than 0")
            quit()
    else:
        print("Pls,enter the correct number next time")
        quit()


    random_number = random.randint(0,number_range)
    guesses = 0
    while random_number != number_range:
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Pls enter the number next time!!!")
            continue

        if user_guess == random_number:
            print("You got it!!")
            break

        elif user_guess > random_number:
            print("You were above the guesses")
        else:
            print("you were below the guesses")
        guesses +=1

    print("you got it in",guesses,"guesses")

number_guess()