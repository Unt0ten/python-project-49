from brain_games.game_logic import game_logic
from random import randint


def game_conditions():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return None


def question_generator():
    question = randint(1, 20)
    return question


def correct_answer(question):
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer


game_logic(game_conditions, question_generator, correct_answer)
