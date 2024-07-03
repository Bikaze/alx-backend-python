#!/usr/bin/env python3
"""
This module provides a function `zoom_array` that replicates
elements in a tuple by a specified factor.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int],
               factor: int = 2) -> List[int]:
    """
    Replicates each element in a tuple by a specified factor.

    Args:
        lst: A list or tuple of integers to be zoomed.
        factor: The replication factor for each element in `lst`.

    Returns:
        A list of integers with each element from the input list or
        tuple replicated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
