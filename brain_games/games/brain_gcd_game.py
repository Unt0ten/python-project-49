from random import randint
import math


def game_conditions():
    print('Find the greatest common divisor of given numbers.')
    return None


def question_generator():
    lower_range_limit = 1
    upper_range_limit = 20
    first_random_number = randint(lower_range_limit, upper_range_limit)
    second_random_number = randint(lower_range_limit, upper_range_limit)
    answer = f'{first_random_number} {second_random_number}'
    return answer


def correct_answer(answer):
    answer = answer.split(' ')
    f_num_ind = 0  # first number index
    s_num_ind = 1  # second number index
    correct_answer = math.gcd(int(answer[f_num_ind]), int(answer[s_num_ind]))
    return str(correct_answer)
