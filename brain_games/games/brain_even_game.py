from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_RANGE_LIMIT = 1
UPPER_RANGE_LIMIT = 20


def question_generator():
    question = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    return question


def correct_answer(question):
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer
