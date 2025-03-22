import quiz_brain
import data
import question_model

question_bank = [question_model.Trivia(question["text"], question["answer"]) for question in data.question_data]

game_status = True

while game_status:
    game_start = input("Do you want to play a game of trivia? press 'y' for yes: ").strip().lower()
    if game_start == "y":
        game_initialize = quiz_brain.QuizBrain(question_bank)
        player_status = True
        while player_status:
            player_status = game_initialize.new_question()
    else:
        game_status = False
