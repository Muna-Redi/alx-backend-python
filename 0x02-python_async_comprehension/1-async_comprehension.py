#!/usr/bin/env python3
""" Python async comprehensions """

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ This function returns 10 random numbers  """
    random_numbers = [x async for x in async_generator()]
    return random_numbers
