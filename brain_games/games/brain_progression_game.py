from random import randint

DESCRIPTION = 'What number is missing in the progression?'
LOWER_RANGE = 2
UPPER_RANGE = 20
START_SEGMENT = 5  # lower bound on the length of an arithmetic progression
END_SEGMENT = 10  # upper bound on the length of an arithmetic progression


def generate_progression(start, finish, step):
    progression_list = [str(n) for n in range(start, finish, step)]
    return progression_list


def get_game_data():
    # the step of the arithmetic progression
    step = randint(LOWER_RANGE, UPPER_RANGE)
    # start of arithmetic progression
    start = randint(LOWER_RANGE, UPPER_RANGE)
    # length of an arithmetic progression
    length = randint(START_SEGMENT, END_SEGMENT)
    finish = start + step * length

    progression_list = generate_progression(start, finish, step)
    missing_item = randint(0, length - 1)
    answer = progression_list[missing_item]
    progression_list[missing_item] = '..'
    question = ' '.join(progression_list)
    return question, str(answer)
