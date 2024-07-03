#!/usr/bin/env python3
"""
This module provides a function `zoom_array` that replicates
elements in a tuple by a specified factor.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Replicates each element in a tuple by a specified factor.

    Args:
        lst: A tuple of integers to be zoomed.
        factor: The replication factor for each element in `lst`.

    Returns:
        A list of integers with each element from the input tuple
        replicated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
