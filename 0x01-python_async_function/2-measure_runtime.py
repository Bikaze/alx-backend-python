#!/usr/bin/env python3
"""
This module measures the execution time of asynchronous functions.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures and returns the average execution time per call of
    the wait_n function.

    Args:
        n (int): The number of times to execute `wait_n`.
        max_delay (int): The maximum delay for `wait_n`.

    Returns:
        float: The average time per call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
