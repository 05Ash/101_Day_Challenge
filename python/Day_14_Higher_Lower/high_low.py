#1> Importing modules
import art
from game_data import data
import random

#2> Art import

#3.1> Function to pick random index
def random_selector(pre_data):
    """Pick a random data, and check if it doesn't match"""
#3.2> length of the data
#3.3> function should include index which it should not pick and pick once more if the index is already picked
#3.3> function should include index which it should not pick and pick once more if the index is already picked
    random_data = random.choice(data)
    while random_data == pre_data:
        random_data = random.choice(data)
    return random_data
#5.1> function to check who has higher and lower
def higher_lower(data1, data2, user_guess):
    """Check if user guess is correct or not and return True of False"""
    if user_guess == "a":
        return data1["follower_count"] > data2["follower_count"]
    return data2["follower_count"] > data1["follower_count"]

def data_formatter(data_dict):
    """Take a dictionary and return name, description, and country in a formatted manner"""
    return f"{data_dict['name']}, a {data_dict['description']}, from {data_dict['country']}."
game_status = True
while game_status:
#4.1> Pick a random person 1

    contendor_B = random_selector(None)
#4.3> Pick a random person 2, while sending the index of person 1
    score = 0
    check_status = True
    while check_status:
        print("\n"*20)
        print(art.logo)
        contendor_A = contendor_B
        contendor_B = random_selector(contendor_A)
#4.2> Vs Art
        print(f"Compare A: {data_formatter(contendor_A)}")
        print(art.vs,"\n")
        print(f"Against B: {data_formatter(contendor_B)}")
#5.2> Take user input between A and B
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while guess not in "ab":
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        check_status = higher_lower(contendor_A, contendor_B, guess)
#5.3> If right increase score and initialize again
        if check_status:
            score += 1
            print(f"You're right. Current score: {score}")
#5.4> If wrong give the score and end the game
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
#5.5> Ask if user want to play again
    game_continue = input("Do you want to play again? Press 'y' for Yes: ")
    if game_continue != 'y':
        game_status = False
