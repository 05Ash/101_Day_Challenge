class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def new_question(self):
        """Picks a question from a list of questions, and if the answer is right
        increase the score by 1 and return True,
        else print the final score and return False"""
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number + 1}. {question.question} True or False: ").strip().title()
        # print(user_answer, question.answer)
        if user_answer == question.answer:
            self.score += 1
            print(f"You're right!\nYour current score is {self.score}")
            return True
        print("You're wrong.\nGame Over!!!")
        print(f"Your final score is {self.score}")
        return False

# from data import question_data
# from random import choice
# from question_model import Trivia

# class QuestionBank:
#     def __init__(self):
#         self.question_bank = question_data
#         self.score = 0

#     def new_question(self):
#         """Picks a question from a list of questions, and if the answer is right
#         increase the score by 1 and return True,
#         else print the final score and return False"""
#         question = choice(self.question_bank)
#         self.question_bank.remove(question)
#         question = Trivia(question["text"], question["answer"])
#         if question.ask_question():
#             self.score += 1
#             print(f"You're right!\nYour current score is {self.score}")
#             return True
#         print("You're wrong.\nGame Over!!!")
#         print(f"Your final score is {self.score}")
#         return False
