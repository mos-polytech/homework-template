# -*- coding: utf-8 -*-

"""
Main file. Contains program execution logic.
"""

from todo.custom_exceptions import UserExitException
from todo.runtime import parse_user_input, perform_command


def main():
    """
    Main method, works infinitely until user runs `exit` command.
    Or hits `Ctrl+C` in the console.
    """
    while True:
        try:
            command = parse_user_input()
            perform_command(command)
        except UserExitException:
            break
        except Exception as e:
            print('You have done something wrong!', e)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
