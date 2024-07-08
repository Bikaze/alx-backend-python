#!/usr/bin/env python3
"""
This module defines a task_wait_n function that returns a list of all the
delays (wait_random) in ascending order without using the wait_n function.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all the delays (wait_random) in ascending order.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = [
        await task for task in asyncio.as_completed(tasks)
    ]
    return completed_tasks
