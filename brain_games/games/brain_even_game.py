from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_RANGE_LIMIT = 1
UPPER_RANGE_LIMIT = 20


def get_game_data():
    question = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
