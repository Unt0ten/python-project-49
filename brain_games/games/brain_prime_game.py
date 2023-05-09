from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_RANGE_LIMIT = 2
UPPER_RANGE_LIMIT = 20


def question_generator():
    question = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    return question


def correct_answer(question):
    divider = 2
    while question % divider != 0:
        divider += 1
    if divider == question:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
