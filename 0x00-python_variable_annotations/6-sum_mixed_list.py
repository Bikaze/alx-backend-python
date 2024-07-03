#!/usr/bin/env python3
"""Module for summing a mixed list of integers and floats.

This module provides a function that sums a list of integers and floats and
returns the total as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        The mixed list of integers and floats to sum.

    Returns:
        float: The sum of the mixed list.
    """
    return sum(mxd_lst)
