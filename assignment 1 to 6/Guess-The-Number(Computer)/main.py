import random

print("Welcome To The Number Guessing Game!")

low = 1
high = 10

print("Think of a number between 1 to 10 and the computer will try to guess it.")

if low <= high:
    guess = random.randint(low, high)
    print("Computer's guess is:", guess)

    while True:
        feedback = input("Is the guess High (H), Low (L), or Correct (C)? ").strip().upper()

        if feedback == 'C':
            print("Yay! The computer guessed your number!")
            break
        elif feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        else:
            print("Invalid input. Please enter H, L or C.")
            continue  

        if low > high:
            print("Hmm, your responses seem inconsistent! Let's try again.")
            break

        guess = random.randint(low, high)
        print("Computer's new guess is:", guess)
