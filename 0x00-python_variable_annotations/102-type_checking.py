#!/usr/bin/env python3
"""
This module provides a function `zoom_array` that replicates
elements in a tuple by a specified factor.
"""

from typing import List, Tuple, Union


from typing import List, Tuple, Union

def zoom_array(lst: Union[Tuple[int, ...], List[int]], factor: int = 2) -> List[int]:
    """
    Replicates each element in a tuple or list by a specified factor.

    Args:
        lst: A list or tuple of integers to be zoomed.
        factor: The replication factor for each element in `lst`.

    Returns:
        A list of integers with each element from the input list or tuple replicated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
