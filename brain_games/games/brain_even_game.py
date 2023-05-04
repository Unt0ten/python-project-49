from random import randint


def game_conditions():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return None


def question_generator():
    lower_range_limit = 1
    upper_range_limit = 20
    question = randint(lower_range_limit, upper_range_limit)
    return question


def correct_answer(question):
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer
