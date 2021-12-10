#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2021 - Day 06 - Challenge 1
https://adventofcode.com/2021/day/06

Solution: 394994
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from collections import deque


def main(ifile='inputs/day_06_input.txt', generations=80, cycle=7, maturity=9):
    population = deque([0,] * maturity)
    with open(ifile) as file:
        for f in file.read().split(','):
            population[int(f)] += 1
    for _ in range(generations):
        population.rotate(-1)  # "Age" the fish and spawn children
        population[cycle-1] += population[-1]  # Re-introduce parents
    result = sum(population)
    print(f"\nAfter {generations} days there would be {result} lanternfish\n")
    return result


if __name__ == "__main__":
    main(generations=80)
