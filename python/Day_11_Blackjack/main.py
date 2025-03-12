import artwork
import random

#1> Intialize deck
deck=["K","Q","J","10","9","8","7","6","5","4","3","2","A"]

#2> Intro question

game_start=(input("Do you want to play a game of Blackjack? Type 'y' for Yes and 'n' for No.")).lower()

#3> Function to draw a card

def draw_card():
    """Draws a random card"""
    card = random.choice(deck)
    return card

#4> Function to calculate score

def card_score(card, score):
    """calculate score for the single card, and adds it to the score"""

    if card in "KQJ":
        return score + 10
    elif card == "A":
        if (score + 1) == 21 or (score + 11) > 21:
            return score + 1
        else:
            return score + 11
    else:
        return score + int(card)

# Function to print card
def print_cards(cards):
    """Print a deck line by line"""
    card_lines = [artwork.deck[card].split("\n") for card in cards]
    length = len(card_lines[0])
    for index in range(length):
        for card in card_lines:
            print(card[index], end="\t")
        print("\n", end="")

# 4.2> Function to append card

#5> Game intialization in while

while game_start == "y":

    print(artwork.intro)

    # Default intialization
    game_end = False
    player_cards=[draw_card(),draw_card()]
    computer_cards=[draw_card()]
    player_score = sum([card_score(card, 0) for card in player_cards])
    computer_score = card_score(computer_cards[0], 0)
    winner = None

    #Intro Cards Prin
    print("\t\tYour Hand: ", " ".join(player_cards), "\t Current Score: ",player_score)
    print_cards(player_cards)
    print("\t\tComputer's First Card: ", computer_cards[0], "\t Current Score: ",computer_score)
    print_cards(computer_cards)

    #Player choices
    while not game_end:
        if player_score == 21:
            game_end = True
            winner = "Player"
            break

        player_choice =  (input("Do you want to draw another card? Press 'y' for yes and 'n' for no: ")).lower()

        if player_choice == "y":

            new_card = draw_card()
            player_cards.append(new_card)
            player_score = card_score(new_card, player_score)
            print(player_score)
            if player_score < 21:

                print("\t\tYour Current Hand: ", " ".join(player_cards), "\t Current Score: ",player_score)
                print_cards(player_cards)
                continue

            if player_score > 21:
                game_end =  True
                winner = "Computer"

        else:
            game_end = True

    # Computer choices
    if winner == None:

        game_end = False

        while not game_end:

            if computer_score < 17:
                new_card = draw_card()
                computer_cards.append(new_card)
                computer_score = card_score(new_card, computer_score)

            else:

                if computer_score == player_score:
                    winner = "Draw"

                elif computer_score == 21 or computer_score > player_score:
                    winner = "Computer"

                elif computer_score > 21 or computer_score < player_score:
                    winner = "Player"
                game_end = True

    print("\t\tYour Final Hand: ", " ".join(player_cards), "\t Final Score: ",player_score)
    print_cards(player_cards)

    if player_score <21: # Print's Computer cards only if they have been drawn
        print("\t\tComputer's Final Hand: ", " ".join(computer_cards),"\t\t", "Computer's Final Score: ",computer_score)
        print_cards(computer_cards)

    if winner == "Draw":
        print("\t\tThe game ended in a draw.")
        game_end = True

    elif winner == "Player":
        print("\t\tYou win!!!")

    else:
        print("\t\tYou Lose!!!")


    game_start=(input("Do you want to play a game of Blackjack? Type 'y' for Yes and 'n' for No.")).lower()
