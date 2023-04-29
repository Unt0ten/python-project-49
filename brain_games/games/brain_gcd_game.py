from brain_games.game_logic import game_logic
from random import randint
import math


def game_conditions():
    print('Find the greatest common divisor of given numbers.')
    return None


def question_generator():
    first_random_number = randint(1, 20)
    second_random_number = randint(1, 10)
    answer = f'{first_random_number} {second_random_number}'
    return answer


def correct_answer(answer):
    answer = answer.split(' ')
    correct_answer = math.gcd(int(answer[0]), int(answer[1]))
    return str(correct_answer)


game_logic(game_conditions, question_generator, correct_answer)
