#!/usr/bin/env python3
"""
Asynchronous generator module.

This module defines an asynchronous generator function that yields
10 random floating-point numbers between 0 and 10, waiting 1 second
between each yield asynchronously.
"""

import random
import asyncio


async def async_generator():
    """
    Asynchronous generator that yields 10 random float numbers between
    0 and 10.

    The generator waits asynchronously for 1 second before yielding each
    number.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
