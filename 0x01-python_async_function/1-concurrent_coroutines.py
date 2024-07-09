#!/usr/bin/env python3
"""
This module demonstrates an asynchronous approach to spawning tasks with
variable delays.

The primary function, `wait_n`, asynchronously waits for a specified number
of tasks, each with a random delay, to complete. The delays are generated in
a way that they do not need to be sorted post-completion, as they are
handled concurrently and collected in the order they finish.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay. Returns delays
    in the order they complete.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delays in the order they were completed.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = [await f for f in asyncio.as_completed(tasks)]
    return delays
