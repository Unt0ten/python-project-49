from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name


# function to determine the parity of a random number
def parity_check_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):  # number of attempts
        random_number = randint(1, 20)
        print(f'Question: {random_number}')  # question asked to the user
        user_response = input()  # user enters a response
        # determine the correct answer
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if user_response != correct_answer:
            break
        else:
            print('Correct!')
    end_game(user_response, correct_answer, name)


def end_game(user_response, correct_answer, name):
    if user_response != correct_answer:
        print(f"'{user_response}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')
