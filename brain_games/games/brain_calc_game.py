from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
LOWER_RANGE_LIMIT = 1
UPPER_RANGE_LIMIT = 20


def get_game_data():
    first_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    second_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    operator = choice(['-', '+', '*'])
    question = f'{first_random_number} {operator} {second_random_number}'
    if '-' in operator:
        answer = first_random_number - second_random_number
    elif '+' in operator:
        answer = first_random_number + second_random_number
    elif '*' in operator:
        answer = first_random_number * second_random_number
    return question, str(answer)
