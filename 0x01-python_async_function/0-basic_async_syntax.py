#!/usr/bin/env python3
'''python async Function '''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        This async function waits for a random
        delay between 0 and max and then returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
