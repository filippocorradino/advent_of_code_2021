#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2021 - Day 08
https://adventofcode.com/2021/day/08

Solution 1: 521
Solution 2: 1016804
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from difflib import SequenceMatcher


SEVEN_SEGMENT = {0: 'abcefg',
                 1: 'cf',
                 2: 'acdeg',
                 3: 'acdfg',
                 4: 'bcdf',
                 5: 'abdfg',
                 6: 'abdefg',
                 7: 'acf',
                 8: 'abcdefg',
                 9: 'abcdfg'}


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def signatures(strings):
    """Returns a list of hashable signatures based on the distance between
    each string and all the other strings in the input vector
    """
    return [tuple(sorted(similar(a, b) for b in strings)) for a in strings]


def main(ifile='inputs/day_08_input.txt'):
    symbols = list(SEVEN_SEGMENT.values())
    lengths = [len(v) for v in symbols]
    unique_lengths = [v for v in lengths if lengths.count(v) == 1]
    sign_to_num = {x: v for x, v in zip(signatures(symbols), SEVEN_SEGMENT)}
    counter = 0
    total = 0
    with open(ifile) as file:
        for line in file:
            pattern, output = ([''.join(sorted(x)) for x in field.split()]
                               for field in line.strip().split(' | '))
            # Part 1
            counter += len([digit for digit in output
                            if len(digit) in unique_lengths])
            # Part 2
            str_to_sign = {x: v for x, v in zip(pattern, signatures(pattern))}
            output_value = [sign_to_num[str_to_sign[x]] for x in output]
            total += int(''.join(str(x) for x in output_value))
    print(f"There are {counter} digits with a unique number of segments")
    print(f"The sum of all 4-digit outputs is {total}")
    return [counter, total]
    

if __name__ == "__main__":
    main()
