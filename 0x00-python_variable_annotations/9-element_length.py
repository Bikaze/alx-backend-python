#!/usr/bin/env python3
"""
This module provides a function `element_length` that calculates
the length of each element in an iterable.
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    each containing an element from the input iterable and its length.

    Args:
        lst: An iterable of sequences.

    Returns:
        A list of tuples, each tuple containing an element
        from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
