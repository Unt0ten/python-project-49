from brain_games.game_logic import game_logic
from random import randint, choice


def game_conditions():
    print('What number is missing in the progression?')
    return None


def question_generator():
    diff_of_an_arith = randint(2, 10)  # the difference of the arithmetic progression
    start_of_arith_prog = randint(1, 40)  # start of arithmetic progression
    length_of_an_arith = randint(5, 10)  # length of an arithmetic progression
    end_of_arith_prog = start_of_arith_prog + diff_of_an_arith * length_of_an_arith
    # create a list of arithmetic sequence
    arithmetic_progression = []
    [arithmetic_progression.append(str(n)) for n in range(start_of_arith_prog, end_of_arith_prog, diff_of_an_arith)]
    i = arithmetic_progression.index(choice(arithmetic_progression))  # the index of the element to be removed
    arithmetic_progression.insert(i, '..')  # replacing random element with '..'
    arithmetic_progression.pop(i + 1)  # random element removal
    answer = ' '.join(arithmetic_progression)
    return answer


def correct_answer(answer):
    answer = answer.split(' ')  # re-forming the list of arithmetic progression
    i = answer.index('..')  # find index of value '..'
    # find difference of arithmetic progression depending on the index
    if i == len(answer) - 1:  # if the index of the difference of the arithmetic progression is the last
        diff_of_an_arith = int(answer[1]) - int(answer[0])
        correct_answer = int(answer[i - 1]) + diff_of_an_arith
    elif i == 0:  # if the index of the difference of the arithmetic progression is the first
        diff_of_an_arith = int(answer[2]) - int(answer[1])
        correct_answer = int(answer[1]) - diff_of_an_arith
    else:  # in other cases
        diff_of_an_arith = int(answer[i + 2]) - int(answer[i + 1])
        correct_answer = int(answer[i + 1]) - diff_of_an_arith
    return str(correct_answer)


game_logic(game_conditions, question_generator, correct_answer)
