import prompt
from random import randint, choice
import operator

def random_operation(first_random_number, second_random_number):
    operator = choice(['-', '+', '*'])
    if operator == '-':
        return operator.sub(first_random_number, second_random_number)
    elif operator == '+:':
        return  operator.add(first_random_number, second_random_number)
    elif operator == '*':
        return operator.mul(first_random_number, second_random_number)


def random_number():
    first_random_number = randint(1, 20)
    second_random_number = randint(1, 20)
    return first_random_number or second_random_number
