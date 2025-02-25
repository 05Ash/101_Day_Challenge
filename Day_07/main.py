import random
from word_list import word_list
import hangman_art

stages=hangman_art.stages

chosen_word=random.choice(word_list).lower()

def hangman(word):

    print()
    word2Guess=["_"]*len(word)
    lives=6
    print(hangman_art.logo)

    while word2Guess.count("_")>0 and lives>0:

        print(f'Word to guess: {"".join(word2Guess)}')
        guess=(input("Guess a letter: ")).lower()

        if not len(guess):
            print("No character was enter, please try again!!!")
            continue
        if guess in word:
            print(f"You guess was {guess}, that's correct!!!")
            word2Guess=[guess if word[index]==guess else char for index, char in enumerate(word2Guess)]

        else:
            lives-=1
            print(f"You guess {guess}, that's not in the word. You lose a life!!!")

        print(f"{stages[len(stages)-(lives)-1]}\n***********************{lives}/6 LIVES LEFT***********************")

    if word2Guess.count("_")==0:
        print(hangman_art.win_art)

    if lives==0:
        print(f"***********************IT WAS {word}! YOU LOSE***********************\n",hangman_art.lose_art)

while (input("Do you want to play hangman (press y for yes): ")).lower()=="y":
    hangman(chosen_word)
