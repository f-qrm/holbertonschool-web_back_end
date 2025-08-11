#!/usr/bin/env python3
"""
This module contains a helper function to calculate index ranges
for paginating datasets.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Return start and end index for pagination.

        Args:
            page (int): 1-indexed page number.
            page_size (int): Number of items per page.

        Returns:
            Tuple[int, int]: (start_index, end_index) slice indices.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
