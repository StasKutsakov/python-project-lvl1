#!/usr/bin/env python

from brain_games.scripts.brain_games import greet
from brain_games.games.brain_progression import find_progression


def main():
    greet()
    find_progression()


if __name__ == '__main__':
    main()
