import random
import artwork

status = True

# 1> A function to pick a number from a range
def number_picker(num=100):
    choice = random.randint(1, num)
    return choice

# 2> A function to compare the guess with the number
def num_compare(guess, answer):
    if guess == answer:
        print(f"You got it right, the number was {guess}!!!")
        return 0

    elif guess > answer:
        print("Too High!!!")
        return 1

    else:
        print("Too Low!!!")
        return -1

# 3> Primary loop to run the game continuously until users says no

while status:
    print(artwork.intro_art)
    print("Welcome to the Number Guessing Game!\nI'm thinking a number between 1 and 100.")
    lives = 10 if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy" else 5
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    actual_guess = number_picker()
    while lives > 0:
        guess_result = num_compare(user_guess, actual_guess)
        if guess_result == 0:
            break
        lives -= 1
        print("Guess again.")
        user_guess = int(input("Make a guess: "))
    if lives == 0 and guess_result != 0:
        print("You lose.")

    status = bool(input("Do you want to play again? Press 'y' for yes: ") == "y")
    print("\n"*20)
