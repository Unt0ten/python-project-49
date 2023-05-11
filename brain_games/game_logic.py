import prompt

NUMBER_OF_ROUNDS = 3


def game_logic(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.DESCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        question, answer = game_module.get_game_data()
        print(f'Question: {question}')
        user_response = input()
        if user_response == answer:
            print('Correct!')
        else:
            print(
                f"'{user_response}' is wrong answer ;(. "
                f"Correct answer was '{answer}'. "
                f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
    exit()
