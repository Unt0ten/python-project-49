#!/usr/bin/env python3

from brain_games.games.brain_even_game import correct_answer
from brain_games.games.brain_even_game import question_generator
from brain_games.games.brain_even_game import game_conditions
from brain_games.game_logic import game_logic


def main():
    game_logic(game_conditions, question_generator, correct_answer)


if __name__ == '__main__':
    main()
