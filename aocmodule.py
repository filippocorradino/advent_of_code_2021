"""
Advent of Code 2022 - Utilities Module
https://adventofcode.com/2021/
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from itertools import tee


def sliding_window(iterable, n=2):
    """
    Creates a sliding window of size n over an iterable object
    Returns a generator of n-tuples
    """
    iterators = tee(iterable, n)
    for i, iterator in enumerate(iterators):
        for _ in range(i):
            next(iterator, None)
    return zip(*iterators)
