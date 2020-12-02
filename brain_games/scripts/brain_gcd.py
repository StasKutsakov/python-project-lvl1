#!/usr/bin/env python

from brain_games.engine import engine
from brain_games.games.brain_gcd import game
from brain_games.games.brain_gcd import rule


def main():
    engine(rule, game)


if __name__ == '__main__':
    main()
