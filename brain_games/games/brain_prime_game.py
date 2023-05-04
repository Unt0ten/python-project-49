from random import randint


def game_conditions():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return None


def question_generator():
    lower_range_limit = 2
    upper_range_limit = 20
    question = randint(lower_range_limit, upper_range_limit)
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
