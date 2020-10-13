#!/usr/bin/env python3


def greeting(string):
    print("{}".format(string))


def main():
    greeting("Welcome to the Brain Games!")
    from brain_games.cli import welcome_user

if __name__ == "__main__":
    main()