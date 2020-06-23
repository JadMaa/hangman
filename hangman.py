# Write your code here
import random

word_list = ["python", "java", "kotlin", "javascript"]
choice = ''

print("H A N G M A N")
while choice != 'exit':
    print("Type \"play\" to play the game, \"exit\" to quit:")
    choice = input()
    if choice == "play":
        answer = random.choice(word_list)
        tries = 8
        answer_list = list(answer)
        letter_set = set()
        updated_answer = "-" * len(answer)

        while tries != 0:
            print("\n" + updated_answer)
            print("Input a letter:>")
            letter = input()
            if len(letter) != 1:
                print("You should input a single letter")
                continue
            if not letter.isalpha() or not letter.islower():
                print("It is not an ASCII lowercase letter")
                continue
            if letter in letter_set:
                print("You already typed this letter")
                continue
            letter_set.add(letter)
            if letter not in answer_list:
                print("No such letter in the word")
                tries -= 1
                if tries == 0:
                    print("You are hanged!")
                    break
                continue
            for index, val in enumerate(answer_list):
                if letter == val:
                    updated_answer = updated_answer[:index] + letter + updated_answer[index + 1:]
            if "-" not in updated_answer:
                print(updated_answer)
                print("You guessed the word!")
                print("You survived!")
                break
