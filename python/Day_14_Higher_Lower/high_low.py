#1> Importing modules
import art
from game_data import data
import random

#2> Art import
print(art.logo)

#3.1> Function to pick random index
def random_selector(pre_index):
#3.2> length of the data
#3.3> function should include index which it should not pick and pick once more if the index is already picked
    length = len(data)
    check = True
#3.3> function should include index which it should not pick and pick once more if the index is already picked
    while check:
        random_index = random.randrange(0, length)
        check = True if pre_index == random_index else False
    return random_index
#5.1> function to check who has higher and lower
def higher_lower(data1, data2, user_guess):
    if user_guess == "a":
        return data1["follower_count"] > data2["follower_count"]
    return data2["follower_count"] > data1["follower_count"]
game_status = True
while game_status:
#4.1> Pick a random person 1
    index_A = random_selector(-1)
    contendor_A = data[index_A]
#4.3> Pick a random person 2, while sending the index of person 1
    index_B = random_selector(index_A)
    contendor_B = data[index_B]
    score = 0
    check_status = True
    while check_status:
#4.2> Vs Art
        print(f"Compare A: {contendor_A['name']}, a {contendor_A['description']}, from {contendor_A['country']}.")
        print(art.vs,"\n")
        print(f"Compare B: {contendor_B['name']}, a {contendor_B['description']}, from {contendor_B['country']}.")
#5.2> Take user input between A and B
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while guess not in "ab":
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        check_status = higher_lower(contendor_A, contendor_B, guess)
#5.3> If right increase score and initialize again
        if check_status:
            score += 1
            index_A, contendor_A = index_B, contendor_B
            index_B = random_selector(index_A)
            contendor_B = data[index_B]
            print(f"You're right. Current score: {score}")
#5.4> If wrong give the score and end the game
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
#5.5> Ask if user want to play again
    print("\n"*20)
    game_continue = input("Do you want to play again? Press 'y' for Yes: ")
    if game_continue != 'y':
        game_status = False
