#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2021 - Day 01
https://adventofcode.com/2021/day/01

Solution 1: 1766
Solution 2: 1797
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import sliding_window


def depth_scanner(ifile, window):
    counter = 0
    with open(ifile) as file:
        depths = (int(x) for x in file)
        for a, b in sliding_window(sliding_window(depths, n=window), n=2):
            if sum(a) < sum(b):
                counter += 1
    print(f"The depth increases {counter} times "
          f"(over a sliding window of size {window})")
    return counter


def main(ifile='inputs/day_01_input.txt', windows=[1, 3]):
    return [depth_scanner(ifile, window) for window in windows]
    

if __name__ == "__main__":
    main()
