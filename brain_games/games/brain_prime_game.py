from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_RANGE_LIMIT = 2
UPPER_RANGE_LIMIT = 20


def get_game_data():
    divider = 2
    question = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    while question % divider != 0:
        divider += 1
    if divider == question:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
