import random

word_list = [
    "Messi", "Ronaldo", "Neymar", "Mbappe", "Lewandowski", "Benzema", "Modric", "Salah", "Kane", "Haaland",
    "Kante", "Suarez", "Ramos", "Alisson", "Courtois", "Mane", "Firmino", "Griezmann", "Hazard", "Pogba",
    "Sterling", "Aguero", "Silva", "Fernandes", "Debruyne", "Lukaku", "Aubameyang", "Lloris", "Oblak", "Varane",
    "Vidal", "Pique", "Dybala", "Chiellini", "Buffon", "Casemiro", "Neuer", "Gundogan", "Kroos", "Cavani",
    "Mahrez", "Pepe", "Thiago", "Werner", "Gomez", "Jota", "Ziyech", "Foden", "Mertens", "Immobile",
    "Benz", "Felix", "Bale", "Martial", "Mount", "Icardi", "Son", "Rodriguez", "Depay", "Tadic",
    "Sancho", "Zaha", "Werner", "Abraham", "Insigne", "Vardy", "Morata", "Keane", "Mina", "Richarlison",
    "Alli", "Arnautovic", "Higuain", "Giroud", "Pulisic", "Rashford", "James", "Maguire", "Reus", "Hummels",
    "Sane", "Robertson", "Fabinho", "Militao", "Alaba", "Goretzka", "Havertz", "Chiesa", "Torres", "Partey",
    "Dembele", "Vinicius", "Barella", "Locatelli", "DiMaria", "Zielinski", "Correa", "Acuna", "Koulibaly", "Grealish"
]

def hangman_printer(lives):
    if lives == 6:
        print(f"""
     __________
     ||/      |
     ||      (_)
     ||
     ||
     ||
    /||\\
  _/_||_\_________
***********************{lives}/6 LIVES LEFT***********************
              """)
    elif lives==5:
        print(f"""
     __________
     ||/      |
     ||      (_)
     ||       |
     ||
     ||
    /||\\
  _/_||_\_________
***********************{lives}/6 LIVES LEFT***********************
              """)
    elif lives==4:
        print(f"""
     __________
     ||/      |
     ||      (_)
     ||     /'|
     ||
     ||
    /||\\
  _/_||_\_________
***********************{lives}/6 LIVES LEFT***********************
              """)
    elif lives==3:
        print(f"""
     __________
     ||/      |
     ||      (_)
     ||     /'|'\\
     ||
     ||
    /||\\
  _/_||_\_________
***********************{lives}/6 LIVES LEFT***********************
              """)
    elif lives==2:
        print(f"""
     __________
     ||/      |
     ||      (_)
     ||     /'|'\\
     ||      .|.
     ||
    /||\\
  _/_||_\_________
***********************{lives}/6 LIVES LEFT***********************
              """)
    elif lives==1:
        print(f"""
     __________
     ||/      |
     ||      (_)
     ||     /'|'\\
     ||      .|.
     ||     /
    /||\\
  _/_||_\_________
***********************{lives}/6 LIVES LEFT***********************
              """)
    elif lives==0:
        print(f"""
     __________
     ||/      |
     ||      (_)
     ||     /'|'\\
     ||      .|.
     ||     /   \\
    /||\\
  _/_||_\_________
""")


def hangman(word):
    print("""

            ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
            ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
            ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
            ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
            ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
            ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
          """)
    word2Guess=["_"]*len(word)
    lives=6
    print(f'Word to guess: {"".join(word2Guess)}')
    while word2Guess.count("_")>0 and lives>0:
        guess=(input("Guess a letter: ")).lower()
        if not len(guess):
            print("No character was enter, please try again!!!")
            continue
        if guess in word:
            print(f"You guess was {guess}, that's correct!!!")
            word2Guess=[guess if word[index]==guess else char for index, char in enumerate(word2Guess)]
            print(f'Word to guess: {"".join(word2Guess)}')
            hangman_printer(lives)
        else:
            lives-=1
            print(f"You guess {guess}, that's not in the word. You lose a life!!!")
            print(f"Word to guess: {''.join(word2Guess)}")
            hangman_printer(lives)
    if word2Guess.count("_")==0:
        print("""
#  ▄██...▄....▄██████▄..███....█▄........▄█.....█▄...▄█..███▄▄▄▄...
#  ███...██▄.███....███.███....███......███.....███.███..███▀▀▀██▄.
#  ███▄▄▄███.███....███.███....███......███.....███.███▌.███...███.
#  ▀▀▀▀▀▀███.███....███.███....███......███.....███.███▌.███...███.
#  ▄██...███.███....███.███....███......███.....███.███▌.███...███.
#  ███...███.███....███.███....███......███.....███.███..███...███.
#  ███...███.███....███.███....███......███.▄█▄.███.███..███...███.
#  .▀█████▀...▀██████▀..████████▀........▀███▀███▀..█▀....▀█...█▀..
#  ................................................................
""")
    if lives==0:
        print(f"""***********************IT WAS {word}! YOU LOSE***********************
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⣶⡆⠀⣰⣿⠇⣾⡿⠛⠉⠁
                ⠀⣠⣴⠾⠿⠿⠀⢀⣾⣿⣆⣀⣸⣿⣷⣾⣿⡿⢸⣿⠟⢓⠀⠀
                ⣴⡟⠁⣀⣠⣤⠀⣼⣿⠾⣿⣻⣿⠃⠙⢫⣿⠃⣿⡿⠟⠛⠁⠀
                ⢿⣝⣻⣿⡿⠋⠾⠟⠁⠀⠹⠟⠛⠀⠀⠈⠉⠀⠉⠀⠀⠀⠀⠀
                ⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣀⢀⣠⣤⣴⣤⣄⠀
                ⠀⠀⠀⠀⣀⣤⣤⢶⣤⠀⠀⢀⣴⢃⣿⠟⠋⢹⣿⣣⣴⡿⠋⠀
                ⠀⠀⣰⣾⠟⠉⣿⡜⣿⡆⣴⡿⠁⣼⡿⠛⢃⣾⡿⠋⢻⣇⠀⠀
                ⠀⠐⣿⡁⢀⣠⣿⡇⢹⣿⡿⠁⢠⣿⠷⠟⠻⠟⠀⠀⠈⠛⠀⠀
                ⠀⠀⠙⠻⠿⠟⠋⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

while (input("Do you want to play hangman (y for yes and n for n): ")).lower()=="y":
    hangman(random.choice(word_list).lower())
