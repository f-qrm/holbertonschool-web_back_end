#!/usr/bin/env python3
"""Measure runtime of asynchronous coroutine"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n.

    This function measures how long it takes to execute the
    wait_n coroutine with `n` tasks and a given `max_delay`,
    then returns the average time per task.

    Args:
        n (int): Number of times to call wait_random concurrently.
        max_delay (int): Maximum delay passed to wait_random.

    Returns:
        float: Average total execution time per task.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
