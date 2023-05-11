from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'
LOWER_RANGE_LIMIT = 2
UPPER_RANGE_LIMIT = 20
LOW_LEN_PROG = 5  # lower bound on the length of an arithmetic progression
UPP_LEN_PROG = 10  # upper bound on the length of an arithmetic progression


def get_game_data():
    # a_prog - arithmetic progression
    # the difference of the arithmetic progression
    d_arith = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    # start of arithmetic progression
    start_a_prog = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    # length of an arithmetic progression
    len_a_prog = randint(LOW_LEN_PROG, UPP_LEN_PROG)
    end_a_prog = start_a_prog + d_arith * len_a_prog
    # create a list of arithmetic sequence
    a_prog = [str(n) for n in range(start_a_prog, end_a_prog, d_arith)]
    i = a_prog.index(choice(a_prog))  # the index of the element to be removed
    answer = a_prog[i]
    a_prog[i] = '..'
    question = ' '.join(a_prog)
    return question, str(answer)
