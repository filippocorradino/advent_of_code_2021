#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2021 - Day 06 - Challenge 1
https://adventofcode.com/2021/day/06

Solution 1: 394994
Solution 2: 1765974267455
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from collections import deque


def simulate(population, days, cycle):
    population = deque(population)
    for _ in range(days):
        population.rotate(-1)  # "Age" the fish and spawn children
        population[cycle-1] += population[-1]  # Re-introduce parents
    result = sum(population)
    print(f"After {days} days there would be {result} lanternfish")
    return result


def main(ifile='inputs/day_06_input.txt', days=[80, 256],
         cycle=7, maturity=9):
    population = [0,] * maturity
    with open(ifile) as file:
        for f in file.read().split(','):
            population[int(f)] += 1
    return [simulate(population, day, cycle) for day in days]
    

if __name__ == "__main__":
    main()
