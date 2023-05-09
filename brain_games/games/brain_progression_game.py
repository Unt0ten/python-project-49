from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'
LOWER_RANGE_LIMIT = 2
UPPER_RANGE_LIMIT = 20
LOW_LEN_PROG = 5  # lower bound on the length of an arithmetic progression
UPP_LEN_PROG = 10  # upper bound on the length of an arithmetic progression
FIR_EL = 0  # first element of the sequence
SEC_EL = 1  # second element of the sequence
THI_EL = 2  # third element of the sequence


def question_generator():
    # a_prog - arithmetic progression
    # the difference of the arithmetic progression
    d_arith = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    # start of arithmetic progression
    start_a_prog = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    # length of an arithmetic progression
    len_a_prog = randint(LOW_LEN_PROG, UPP_LEN_PROG)
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
    if i == len(answer) - 1 or i == len(answer) - 2:
        diff_of_an_arith = int(answer[SEC_EL]) - int(answer[FIR_EL])
        correct_answer = int(answer[i - 1]) + diff_of_an_arith
    # if the index of the difference of the arithmetic progression is the first:
    elif i == 0:
        diff_of_an_arith = int(answer[THI_EL]) - int(answer[SEC_EL])
        correct_answer = int(answer[SEC_EL]) - diff_of_an_arith
    else:  # in other cases
        diff_of_an_arith = int(answer[i + 2]) - int(answer[i + 1])
        correct_answer = int(answer[i + 1]) - diff_of_an_arith
    return str(correct_answer)
