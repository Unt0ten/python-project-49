from brain_games.game_logic import game_logic
from random import randint


def game_conditions():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return None


def question_generator():
    question = randint(2, 20)
    return question


def correct_answer(question):
    divider = 2
    while question % divider != 0:
        divider += 1
    if divider == question:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


game_logic(game_conditions, question_generator, correct_answer)
