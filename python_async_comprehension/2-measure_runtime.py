#!/usr/bin/env python3
"""
measure_runtime module

Measures execution time of async_comprehension run 4 times in parallel.
"""

import asyncio
from time import time
from typing import Callable

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times in parallel using asyncio.gather,
    and measures the total time taken.

    Returns:
        float: total execution time in seconds.
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
