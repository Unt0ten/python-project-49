from brain_games.game_logic import game_logic
from random import randint, choice


def game_conditions():
    print('What is the result of the expression?')
    return None


def question_generator():
    first_random_number = randint(1, 20)
    second_random_number = randint(1, 10)
    operator = choice(['-', '+', '*'])
    answer = f'{first_random_number} {operator} {second_random_number}'
    return answer


def correct_answer(answer):
    answer = answer.split(' ')
    if '-' in answer[1]:
        correct_answer = int(answer[0]) - int(answer[2])
    elif '+' in answer[1]:
        correct_answer = int(answer[0]) + int(answer[2])
    elif '*' in answer[1]:
        correct_answer = int(answer[0]) * int(answer[2])
    return str(correct_answer)


game_logic(game_conditions, question_generator, correct_answer)
