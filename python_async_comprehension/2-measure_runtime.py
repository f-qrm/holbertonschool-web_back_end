#!/usr/bin/env python3
"""
Measure runtime module.

This module measures the total runtime of running four
instances of async_comprehension concurrently.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times in parallel and measure total runtime.

    Returns:
        float: Total time in seconds taken to run four async_comprehension
        calls concurrently.
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.perf_counter()
    return end - start
