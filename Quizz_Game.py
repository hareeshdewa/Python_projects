
print("Welcome to Quizz Game!!!")
answer_list = ["Random Access Memory", "Read Only Memory", "Graphics Processing Unit", "Central Processing Unit"]
def quizz_game():
    UserPlay = input("Do you want to play? ")

    if UserPlay.lower() != "Y".lower():
        quit()

    print("Let's play then!!!!")
    score = 0

    while True:
        question_one = input("What does RAM stand for? ")
        if question_one.lower() == answer_list[0].lower():
            print("Correct answer!")
            score += 1
            # score = score + 1
        else:
            print("Incorrect!")

        question_Two = input("what does ROM stand for? ")
        if question_Two.lower() == answer_list[1].lower():
            print("Correct answer!!")
            score += 1
        else:
            print("Incorrect!")

        question_Three = input("what does GPU stand for? ")
        if question_Three.lower() == answer_list[2].lower():
            print("Correct answer!!!")
            score += 1
        else:
            print("Incorrect!")

        question_four = input("What does CPU stand for? ")
        if question_four.lower() == answer_list[3].lower():
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect!")

        print('You got ' + str(score) + ' questions correct!!')
        percentage = score / 4 * 100
        print('You got ' + str(percentage) + '% correct!!')

        if percentage > 50:
            print("well done, You have done a good job :)")
            break

        else:
            additional_guess_list = ["File Transfer Protocol","Domain Name System","Simple Mail Transfer Protocol","Hard Disk Drive"]
            while True:
                scores = 0
                if percentage <=50:
                    print("Could have scored better :(")
                    attempt = input("Would you like to play again? ")
                    if attempt.lower() != "y":
                        print("thanks for attempting, See you again :)")
                        quit()

                    print("This time the questions differs!!")
                    print("Let's do this time :)")

                    addition_questions = input("what does FTP stand for? ")
                    if addition_questions.lower() == additional_guess_list[0].lower():
                        print("correct answer!!")
                        scores += 1
                    else:
                        print("Incorrect:(")
                    addition_questions = input("What does DNS stand for? ")
                    if addition_questions.lower() == additional_guess_list[1].lower():
                        print("Correct answer!!")
                        scores += 1
                    else:
                        print("Incorrect:(")
                    addition_questions = input("What does SMTP stand for? ")
                    if addition_questions.lower() == additional_guess_list[2].lower():
                        print("Correct answer, you are doing well!")
                        scores += 1
                    else:
                        print("Incorrect :(")
                    addition_questions = input("what does HDD stand for? ")
                    if addition_questions.lower() == additional_guess_list[3].lower():
                        print("correct answer!!")
                        scores += 1
                    else:
                        print("Incorrect :(")
                    break
            print("You got " + str(scores) + " correct:)")
            print("Your final attempt score is ",str((scores / 4) * 100))
            print("well done :)")
        break
quizz_game()
