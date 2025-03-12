import artwork
import random

#1> Intialize deck

#2> Intro question

game_start=(input("Do you want to play a game of Blackjack? Type 'y' for Yes and 'n' for No.")).lower()

#3> Function to draw a card

def draw_card():
    """Draws a random card"""
    card = random.choice(deck)
    deck.remove(card)
    return card

#4> Function to calculate score

def card_score(cards, score):
    """calculate score for the single card, and adds it to the score"""
    score = 0
    for card in cards:
        if card == "A":
            score += 11
        elif card in "KQJ":
            score += 10
        else:
            score += int(card)

    total_A = cards.count("A")
    # Changing A's score to 0 for all A more than 1
    while total_A > 0 and score > 21:
        score -= 10
        total_A -= 1

    return score

# Function to print card
def print_cards(cards):
    """Print a deck line by line"""
    card_lines = [artwork.deck[card].split("\n") for card in cards]
    length = len(card_lines[0])
    for index in range(length):
        for card in card_lines:
            print(card[index], end="\t")
        print("\n", end="")


# 4.3> Compare function

def compare_score(userS, dealerS):
    if computer_score == player_score:
        return "Draw"

    elif computer_score == 21 or computer_score > player_score:
        return "Computer"

    elif computer_score > 21 or computer_score < player_score:
        return "Player"

#5> Game intialization in while

while game_start == "y":
    deck=[
      "K","Q","J","10","9","8","7","6","5","4","3","2","A",
      "K","Q","J","10","9","8","7","6","5","4","3","2","A",
      "K","Q","J","10","9","8","7","6","5","4","3","2","A",
      "K","Q","J","10","9","8","7","6","5","4","3","2","A",]


    print(artwork.intro)

    # Default intialization
    game_end = False
    player_cards=[]
    computer_cards=[]
    for _ in range(2):
        player_cards.append(draw_card())
        computer_cards.append(draw_card())
    player_score = card_score(player_cards, 0)
    computer_score = card_score(computer_cards, 0)
    winner = None

    #Intro Cards Prin
    print("\t\tYour Hand: ", " ".join(player_cards), "\t Current Score: ",player_score)
    print_cards(player_cards)
    print("\t\tComputer's First Card: ", computer_cards[0])
    print_cards(computer_cards[:1])

    #Player choices
    while not game_end and player_score < 21:

        player_choice =  (input("Do you want to draw another card? Press 'y' for yes and 'n' for no: ")).lower()
        if player_choice == "y":
            player_cards.append(draw_card())
            player_score = card_score(player_cards, player_score)

            if player_score >= 21:
                game_end =  True

            else:
                print("\t\tYour Current Hand: ", " ".join(player_cards), "\t Current Score: ", player_score)
                print_cards(player_cards)

        else:
            game_end = True

    # Computer choices
    while computer_score < 17 and player_score != 21:
        computer_cards.append(draw_card())
        computer_score = card_score(computer_cards, computer_score)

    print("\t\tYour Final Hand: ", " ".join(player_cards), "\t Final Score: ",player_score)
    print_cards(player_cards)
    if player_score <21: # Print's Computer cards only if they have been drawn
        print("\t\tComputer's Final Hand: ", " ".join(computer_cards),"\t\t", "Computer's Final Score: ",computer_score)
        print_cards(computer_cards)

    winner = compare_score(player_score, computer_score)
    if winner == "Draw":
        print("\t\tThe game ended in a draw.")
        game_end = True
    elif winner == "Player":
        print("\t\tYou win!!!")
    else:
        print("\t\tYou Lose!!!")
    game_start=(input("Do you want to play a game of Blackjack? Type 'y' for Yes and 'n' for No.")).lower()
    print("\n"*20)
