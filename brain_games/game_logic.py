import prompt


def game_logic(game_conditions, question_generator, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    game_conditions()
    for _ in range(3):
        question = question_generator()
        print(f'Question: {question}')
        user_response = input()
        if user_response == correct_answer(question):
            print('Correct!')
        else:
            print(
                f"'{user_response}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer(question)}'. "
                f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
    exit()
