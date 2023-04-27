from brain_games.game_logic import game_logic
from random import randint


game_conditions = 'Answer "yes" if the number is even, otherwise answer "no".'
answer = randint(1, 20)
correct_answer = 'yes' if answer % 2 == 0 else 'no'
game_logic(game_conditions, answer, correct_answer)
