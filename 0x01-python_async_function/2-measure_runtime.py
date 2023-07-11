#!/usr/bin/env python3
""" Python async """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ This function Measures the runtime """
    start = time()

    run(wait_n(n, max_delay))

    stop = time()

    return (stop - start) / n
