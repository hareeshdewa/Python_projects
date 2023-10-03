import random
print("Welcome to this game!!!!!!!!")
def Retry_game(func):
    def wrapper():
        func()
        while True:
            attempt = input("Type Y to continue, or Press N to quit: ")
            if attempt == 'Y'.lower():
                func()
            else:
                if attempt == 'N'.lower():
                    print("Bye :)")
                    break
    return wrapper

@Retry_game
def rock_paper_scissors():
    user_wins = 0
    computer_wins = 0
    list_of_items = ['rock', 'paper','scissors']

    while True:
        user_input = input("Type Rock/Paper/Scissors: ").lower()
        if user_input == "Q".lower():
            break

        if user_input not in list_of_items:
            print("Type the provided words")
            continue
        random_number = random.randint(0,2)
        # 0 : rock, paper : 1, scissors :  2

        computer_pick = list_of_items[random_number]

        if user_input == 'rock' and computer_pick == 'scissors':
            print("you won!")
            user_wins +=1

        elif user_input == 'paper' and computer_pick == 'rock':
            print("You won!")
            user_wins+=1

        elif user_input == 'scissors' and computer_pick == 'paper':
            print("You won!")
            user_wins +=1

        else:
            print("You Lost!")
            computer_wins +=1

    print("You won",user_wins,"times")
    print("The computer won",computer_wins,"times")
rock_paper_scissors()

