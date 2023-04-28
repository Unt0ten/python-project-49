import prompt


def game_logic(game_conditions, question, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    print(game_conditions)
    for _ in range(3):
        print(f'Question: {question()}')
        user_response = input()
        if user_response == correct_answer(question):
            print('Correct!')
        else:
            print(
                f"'{user_response}' is wrong answer ;(. Correct answer was '{correct_answer(question)}'. Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
    exit()
