#!/usr/bin/env python3
import random
import asyncio

"""
This module provides an asynchronous function to wait for a random delay.

It demonstrates the use of async/await syntax, random delay generation,
and type annotations in Python.
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay time waited, as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
