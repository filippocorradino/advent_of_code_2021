#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2021 - Day 03
https://adventofcode.com/2021/day/03

Solution 1: 3847100
Solution 2: 4105235
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from aocmodule import sumiter


def process_report(ifile, filter=''):
    
    def line2ints(line):
        # HACK Add 1 at the start to compute the number of processed lines
        return (1,) + tuple(int(x) for x in list(line))
    
    with open(ifile) as file:
        report = (line2ints(line.strip()) for line in file
                            if line.startswith(filter))
        report_totals = list(sumiter(*report))
    report_lines = report_totals.pop(0)  # See HACK in line2ints
    bits_frequency = [x / report_lines for x in report_totals]
    return bits_frequency, report_lines


def report_values_extractor(ifile, antimode=False):

    def binlist2dec(l):
        return int(''.join(str(int(x)) for x in l), 2)

    bits_frequency, report_lines = process_report(ifile)
    bits_mode = [int(x >= 0.5) for x in bits_frequency]
    if antimode:
        bits_mode = [1 - x for x in bits_mode]
    result_0 = binlist2dec(bits_mode)
    filter = ''
    while report_lines > 1:
        new_filter_bit = (bits_frequency[len(filter)] >= 0.5)
        if antimode:
            new_filter_bit = not(new_filter_bit)
        filter += str(int(new_filter_bit))
        bits_frequency, report_lines = process_report(ifile, filter)
    result_1 = binlist2dec(bits_frequency)
    return result_0, result_1


def main(ifile='inputs/day_03_input.txt'):

    gamma_rate, gen_O2_rating = report_values_extractor(ifile, antimode=False)
    epsilon_rate, gen_CO2_rating = report_values_extractor(ifile, antimode=True)
    
    power_consumption = gamma_rate * epsilon_rate
    print(f"The gamma rate is {gamma_rate} "
          f"and epsilon rate is {epsilon_rate}. "
          f"Power consumption is {power_consumption}")
    
    life_support_rating = gen_O2_rating * gen_CO2_rating
    print(f"The O2 generation rating is {gen_O2_rating} "
          f"and CO2 generation rating is {gen_CO2_rating}. "
          f"Life support rating is {life_support_rating}")

    return [power_consumption, life_support_rating]


if __name__ == "__main__":
    main()
