import prompt

ROUNDS_COUNT = 3


def start_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.DESCRIPTION)
    for _ in range(ROUNDS_COUNT):
        question, answer = game_module.get_game_data()
        user_response = prompt.string(f'Question: {question}  ')
        if user_response == answer:
            print('Correct!')
        else:
            print(
                f"'{user_response}' is wrong answer ;(. "
                f"Correct answer was '{answer}'. "
                f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    return
