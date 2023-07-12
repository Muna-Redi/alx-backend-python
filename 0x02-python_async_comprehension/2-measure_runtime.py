#!/usr/bin/env python3
""" Python async comprehensions """

from time import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ This function measures the runtime for
        4 parallel async comprehensions
    """
    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    stop = time()
    return (stop - start)
