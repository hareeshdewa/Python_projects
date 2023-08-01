# Valid Anagram:
# A program to check whether it is an anagram:

def isAnagram():
    first_word = input("Enter the first word: ")
    second_word = input("Enter the second word: ")

    if len(first_word) != len(second_word):
        return "The lengths are not equal"

    for first in first_word:
        for second in second_word:
            if second not in first_word and first not in second_word:
                return False
    return True

print(isAnagram())

while True:
    another_Attempt = input("Would you like to continue it: ")
    if another_Attempt == "Y".lower():
        print(isAnagram())
    else:
        print("That's it, see you :)")
        break
