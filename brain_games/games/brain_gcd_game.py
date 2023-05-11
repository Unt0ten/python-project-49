from random import randint
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LOWER_RANGE_LIMIT = 1
UPPER_RANGE_LIMIT = 20


def get_game_data():
    first_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    second_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    question = f'{first_random_number} {second_random_number}'
    answer = math.gcd(first_random_number, second_random_number)
    return question, str(answer)
