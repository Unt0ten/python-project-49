from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
LOWER_RANGE_LIMIT = 1
UPPER_RANGE_LIMIT = 20
F_NUM_INDEX = 0  # first number index
S_NUM_INDEX = 2  # second number index
OPERATOR_INDEX = 1


def question_generator():
    first_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    second_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    operator = choice(['-', '+', '*'])
    answer = f'{first_random_number} {operator} {second_random_number}'
    return answer


def correct_answer(answer):
    answer = answer.split(' ')
    if '-' in answer[OPERATOR_INDEX]:
        correct_answer = int(answer[F_NUM_INDEX]) - int(answer[S_NUM_INDEX])
    elif '+' in answer[OPERATOR_INDEX]:
        correct_answer = int(answer[F_NUM_INDEX]) + int(answer[S_NUM_INDEX])
    elif '*' in answer[OPERATOR_INDEX]:
        correct_answer = int(answer[F_NUM_INDEX]) * int(answer[S_NUM_INDEX])
    return str(correct_answer)
