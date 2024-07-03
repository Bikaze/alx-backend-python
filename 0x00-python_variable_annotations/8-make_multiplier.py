#!/usr/bin/env python3
"""
This module defines a function that creates a multiplier function.

The `make_multiplier` function takes a single float argument, `multiplier`,
and returns a new function. This returned function takes a float as its
argument and returns the product of this argument and the `multiplier`.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies its input by
        `multiplier`.
    """
    return lambda x: x * multiplier
