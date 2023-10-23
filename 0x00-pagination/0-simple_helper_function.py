#!/usr/bin/env python3
"""
    calculating the offset and end index
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Given the page number and page size,
        The function returns the start and end indexes
        as a tuple
    """
    start = page_size * (page - 1)
    return (start, start + page_size)
