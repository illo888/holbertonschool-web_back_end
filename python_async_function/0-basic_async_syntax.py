#!/usr/bin/env python3
"""
Module that provides an asynchronous function
that waits for a random delay and returns it.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay seconds
    and return the delay as a float.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
