#!/usr/bin/env python3
"""
This module provides a function to return the length of elements
in an iterable sequence. It demonstrates the use of complex type
annotations with duck typing principles.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing elements of the input iterable
    and their respective lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-like elements
        (e.g. list, str, tuple, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing
        an element from the input and its length.
    """
    return [(i, len(i)) for i in lst]
