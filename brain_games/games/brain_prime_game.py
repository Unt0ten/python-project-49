from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_RANGE_LIMIT = 2
UPPER_RANGE_LIMIT = 20


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_game_data():
    question = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
