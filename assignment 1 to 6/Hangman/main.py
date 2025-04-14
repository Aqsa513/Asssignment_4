import random

stages = ['''
    ---------
    |       |
    |
    |
    |
    |
    ---------
''',
'''
    ----------
    |        |
    |        0
    |
    |
    |
    ----------
''',
'''
    ----------
    |        |
    |        0
    |        |
    |
    |
    ----------
''',
'''
    ----------
    |        |
    |        0
    |       /|
    |
    |
    ----------
''',
'''
    ----------
    |        |
    |        0
    |       /|\\
    |
    |
    ----------
''', 
'''
    ----------
    |        |
    |        0
    |       /|\\
    |        /
    |
    ----------
''',
'''
    -----------
    |         |
    |         0
    |        /|\\
    |         / \\
    |
    -----------
''']

words = ["apple", "banana","orange","grapes","peach", "kiwi","pear","plum","berry","mango"]

chosen_word = random.choice(words)
word_display = ['_'for _ in chosen_word]
guess_letters = []
lives = len(stages)-1

print("Welcome to Hangman!")
print("Guess the fruits words.")

while True:
    print("".join(word_display))
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid letter.\n")
        continue

    guess_letters.append(guess)

    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        print(stages[len(stages) - lives -1])
        lives -= 1
        print(f"you have {lives} lives left.")
        if lives == 0 :
            print(stages[lives])
            print(f"You Lose! The word was '{chosen_word}'. ")
            break













