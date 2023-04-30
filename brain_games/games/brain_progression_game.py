from brain_games.game_logic import game_logic
from random import randint, choice


def game_conditions():
    print('What number is missing in the progression?')
    return None


def question_generator():
    # a_prog - arithmetic progression
    d_arith = randint(2, 10)  # the difference of the arithmetic progression
    start_a_prog = randint(1, 40)  # start of arithmetic progression
    len_a_prog = randint(5, 10)  # length of an arithmetic progression
    end_a_prog = start_a_prog + d_arith * len_a_prog
    # create a list of arithmetic sequence
    a_prog = []
    [a_prog.append(str(n)) for n in range(start_a_prog, end_a_prog, d_arith)]
    i = a_prog.index(choice(a_prog))  # the index of the element to be removed
    a_prog.insert(i, '..')  # replacing random element with '..'
    a_prog.pop(i + 1)  # random element removal
    answer = ' '.join(a_prog)
    return answer


def correct_answer(answer):
    answer = answer.split(' ')  # re-forming the list of arithmetic progression
    i = answer.index('..')  # find index of value '..'
    # find difference of arithmetic progression depending on the index
    # if the index of the difference of the arithmetic progression is the last:
    if i == len(answer) - 1:
        diff_of_an_arith = int(answer[1]) - int(answer[0])
        correct_answer = int(answer[i - 1]) + diff_of_an_arith
    # if the index of the difference of the arithmetic progression is the first:
    elif i == 0:
        diff_of_an_arith = int(answer[2]) - int(answer[1])
        correct_answer = int(answer[1]) - diff_of_an_arith
    else:  # in other cases
        diff_of_an_arith = int(answer[i + 2]) - int(answer[i + 1])
        correct_answer = int(answer[i + 1]) - diff_of_an_arith
    return str(correct_answer)


game_logic(game_conditions, question_generator, correct_answer)
