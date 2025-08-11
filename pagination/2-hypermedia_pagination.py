#!/usr/bin/env python3
"""
This module contains a helper function to calculate index ranges
for paginating datasets.
"""
from typing import Tuple
import csv
from math import ceil
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset based on the page number and page size.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows representing the requested page from
            the dataset.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        page_data = dataset[start:end]
        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return pagination info and data for a given page.

        Args:
            page (int): Current page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            dict: Contains page_size, page, data, next_page, prev_page, and
            total_pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = ceil(total_items / page_size)
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
