from random import randint
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LOWER_RANGE_LIMIT = 1
UPPER_RANGE_LIMIT = 20
F_NUM_IND = 0  # first number index
S_NUM_IND = 1  # second number index


def question_generator():
    first_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    second_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    answer = f'{first_random_number} {second_random_number}'
    return answer


def correct_answer(answer):
    answer = answer.split(' ')
    correct_answer = math.gcd(int(answer[F_NUM_IND]), int(answer[S_NUM_IND]))
    return str(correct_answer)
