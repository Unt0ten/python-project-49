from brain_games.parity_check import parity_check_game
from brain_games.parity_check import welcome_user

#!/usr/bin/env python3


def main():
    print('Welcome to the Brain Games!')
    welcome_user(main)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    parity_check_game()



if __name__ == '__main__':
    main()
