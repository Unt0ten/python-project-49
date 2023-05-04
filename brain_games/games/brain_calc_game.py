from random import randint, choice


def game_conditions():
    print('What is the result of the expression?')
    return None


def question_generator():
    lower_range_limit = 1
    upper_range_limit = 20
    first_random_number = randint(lower_range_limit, upper_range_limit)
    second_random_number = randint(lower_range_limit, upper_range_limit)
    operator = choice(['-', '+', '*'])
    answer = f'{first_random_number} {operator} {second_random_number}'
    return answer


def correct_answer(answer):
    answer = answer.split(' ')
    f_num_index = 0  # first number index
    s_num_index = 2  # second number index
    operator_index = 1
    if '-' in answer[operator_index]:
        correct_answer = int(answer[f_num_index]) - int(answer[s_num_index])
    elif '+' in answer[operator_index]:
        correct_answer = int(answer[f_num_index]) + int(answer[s_num_index])
    elif '*' in answer[operator_index]:
        correct_answer = int(answer[f_num_index]) * int(answer[s_num_index])
    return str(correct_answer)
