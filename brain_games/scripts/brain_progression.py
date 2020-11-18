#!/usr/bin/env python

from brain_games.scripts.brain_games import greet
from brain_games.engine import engine
from brain_games.games.brain_progression import game


def main():
    greet()
    engine(game)


if __name__ == '__main__':
    main()
