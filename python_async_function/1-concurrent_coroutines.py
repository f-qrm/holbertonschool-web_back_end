#!/usr/bin/env python3
"""Execute multiple coroutines concurrently and return delays in order of
completion"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and collect results

    This function runs multiple instances of the wait_random coroutine
    concurrently using asyncio.as_completed to collect the results as
    they complete. It returns the list of delays in the order of completion
    (ascending), without explicitly sorting.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay that each coroutine can take.

    Returns:
        List[float]: List of all the delays, in order of completion.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    res = []
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        res.append(result)
    return res
