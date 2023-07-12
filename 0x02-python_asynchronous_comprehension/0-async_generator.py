#!/usr/bin/env python3
""" Python async comprehensions """

from asyncio import sleep
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ This python async function generates
        random number between 0 and 10
    """
    for _ in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
