#!/usr/bin/env python3
"""
This module defines a task_wait_random function that returns an asyncio.Task.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task from the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay argument to pass to wait_random.

    Returns:
        asyncio.Task: The created asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
