#!/usr/bin/env python3
""" Python async  """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ This function creates task from wait_random
        async function and returns the task
    """
    async_task = create_task(wait_random(max_delay))
    return async_task
