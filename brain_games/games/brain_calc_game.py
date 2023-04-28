from brain_games.game_logic import game_logic
from random import randint, choice


def game_conditions():
    print('What is the result of the expression?')
    return None


def question_generator():
    first_random_number = randint(1, 20)
    second_random_number = randint(1, 20)
    operator = choice(['-', '+', '*'])
    question = f'{first_random_number} {operator} {second_random_number}'
    return question


def correct_answer(question):
    if question in '-':
        correct_answer = first_random_number - second_random_number
    elif question in '+:':
        correct_answer = first_random_number + second_random_number
    elif question in '*':
        correct_answer = first_random_number * second_random_number
    return correct_answer

game_logic(game_conditions, question_generator, correct_answer)
