#!/usr/bin/env python3
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    coroutines = [wait_random(max_delay) for _ in range(n)]
    res = []
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        res.append(result)
    return res
