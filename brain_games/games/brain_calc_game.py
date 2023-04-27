from brain_games.game_logic import game_logic
from random import randint, choice

game_conditions = 'What is the result of the expression?'
first_random_number = randint(1, 20)
second_random_number = randint(1, 20)

operator = choice(['-', '+', '*'])
if operator == '-':
    result = first_random_number - second_random_number
elif operator == '+:':
    result = first_random_number + second_random_number
elif operator == '*':
    result = first_random_number * second_random_number
answer = f'{first_random_number} {operator} {second_random_number}'
correct_answer = str(result)
game_logic(game_conditions, answer, correct_answer)
