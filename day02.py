#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2021 - Day 02
https://adventofcode.com/2021/day/02

Solution 1: 2117664
Solution 2: 2073416724
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


MOVEMENTS_DICT_1 = {
    'forward': lambda h, d, _, s: (h+s, d, 0),
    'down': lambda h, d, _, s: (h, d+s, 0),
    'up': lambda h, d, _, s: (h, d-s, 0)
}

MOVEMENTS_DICT_2 = {
    'forward': lambda h, d, a, s: (h+s, d+s*a, a),
    'down': lambda h, d, a, s: (h, d, a+s),
    'up': lambda h, d, a, s: (h, d, a-s)
}


def sail(ifile, movements_dict):
    horizontal, depth, aim = 0, 0, 0
    with open(ifile) as file:
        for line in file:
            direction, step = line.split()
            horizontal, depth, aim = \
                movements_dict[direction](horizontal, depth, aim, int(step))
    result = horizontal * depth
    print(f"The depth is {depth} and horizontal position is {horizontal}, "
          f"their product is {result}")
    return result


def main(ifile='inputs/day_02_input.txt'):
    return [sail(ifile, d) for d in (MOVEMENTS_DICT_1, MOVEMENTS_DICT_2)]


if __name__ == "__main__":
    main()
