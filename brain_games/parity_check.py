from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name

name = welcome_user()

# function to determine the parity of a random number
def parity_check_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):  # number of attempts
        random_number = randint(1, 20)
        print(f'Question: {random_number}')  # question asked to the user
        global user_response
        user_response = input()  # user enters a response
        # determine the correct answer
        global correct_answer
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if user_response != correct_answer:
            break
        else:
            print('Correct!')
    end_game()
    return user_response, correct_answer

def end_game():
    if user_response != correct_answer:
        print(f"'{user_response}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')
