from brain_games.game_logic import game_logic
from random import randint


def question():
    random_number = randint(1, 20)
    return random_number


def correct_answer(question):
    correct_answer = 'yes' if question() % 2 == 0 else 'no'
    return correct_answer

game_conditions = 'Answer "yes" if the number is even, otherwise answer "no".'

game_logic(game_conditions, question, correct_answer)
