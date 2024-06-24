#!/usr/bin/env python3
"""0-simple_helper_function.py"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """get index range"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
