from gui import Game
from services import Game_Data

app = Game()
game_data = Game_Data()

# Game Logic
def start_game():
    level = app.level_var.get()
    game_data.load_data(level)
    game_data.random_question()
    question_display()

def stop_game():
    if app.flip_timer:
        app.canvas.after_cancel(app.flip_timer)
    app.show_question("Score", f"{game_data.score}/{game_data.count}")



def right_guess():
    if app.flip_timer:
        app.canvas.after_cancel(app.flip_timer)
    game_data.correctly_guessed_word.append(game_data.chinese)
    game_data.data.pop(game_data.current)
    game_data.score += 1
    game_data.question_remaining -= 1
    if game_data.question_remaining > 0:
        game_data.random_question()
        question_display()
    else:
        stop_game()


def wrong_guess():
    game_data.random_question()
    question_display()

def question_display():
    if app.flip_timer:
        app.canvas.after_cancel(app.flip_timer)
    app.show_question(game_data.chinese, game_data.pinyin)
    app.flip_timer = app.canvas.after(3000, answer_display)

def answer_display():
    app.show_answer(game_data.english, game_data.parts_of_speech)
    app.flip_timer = ""



# Config Buttons
app.start_button.config(command=start_game)
app.stop_button.config(command=stop_game)
app.right_button.config(command=right_guess)
app.wrong_button.config(command=wrong_guess)



app.run()
