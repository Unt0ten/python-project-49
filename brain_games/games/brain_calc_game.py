from brain_games.game_logic import game_logic
from random import randint, choice

game_conditions = 'What is the result of the expression?'


def question():
    first_random_number = randint(1, 20)
    second_random_number = randint(1, 20)
    operator = choice(['-', '+', '*'])
    print(f'{first_random_number} {operator} {second_random_number}')
    if operator == '-':
        result = first_random_number - second_random_number
    elif operator == '+:':
        result = first_random_number + second_random_number
    elif operator == '*':
        result = first_random_number * second_random_number
    return result

correct_answer =

game_logic(game_conditions, question, correct_answer)
