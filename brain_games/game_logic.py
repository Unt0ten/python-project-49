import prompt
from random import randint, choice

def game_logic(game_conditions, answer, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    print(game_conditions)
    for _ in range(3):
        print(f'Question: {answer}')
        user_response = input()
        if user_response == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_response}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
    exit()
