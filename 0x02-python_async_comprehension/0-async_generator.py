#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields a random number.
"""

import asyncio
import random
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """
    An asynchronous generator that waits 1 second, then yields a random number
    between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
