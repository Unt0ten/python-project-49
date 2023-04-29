from random import randint, choice

def question_generator():
    diff_of_an_arith = randint(2, 10)
    start_of_arith_prog = randint(1, 40)
    length_of_an_arith = randint(5, 10)
    end_of_arith_prog = start_of_arith_prog + diff_of_an_arith * length_of_an_arith
    arithmetic_progression = list(range(start_of_arith_prog, end_of_arith_prog, diff_of_an_arith))
    i = arithmetic_progression.index(choice(arithmetic_progression))  # the index of the element to be removed
    arithmetic_progression.insert(i, '..')  # replacing random element with '..'
    arithmetic_progression.pop(i + 1)  # random element removal
    answer = ' '.join(arithmetic_progression)
    return answer