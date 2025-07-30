#!/usr/bin/env python3
"""
Async comprehension module.

Defines a coroutine that collects 10 random numbers
from an asynchronous generator using async
comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list of 10 random float numbers generated
        asynchronously.
    """
    return [number async for number in async_generator()]
