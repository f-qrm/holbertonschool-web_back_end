#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier function.

It demonstrates the use of function return annotations with Callable
from the typing module.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies its input
        by the multiplier.
    """
    return lambda x: x * multiplier
