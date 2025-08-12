#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            """
            Return a page with deletion-resilient pagination.

            Args:
                index (int): Start index (0 if None).
                page_size (int): Items per page.

            Returns:
                dict: index, next_index, page_size, data.
            """
            if index is None:
                 index = 0

            assert isinstance(index, int) and index >= 0

            dataset = self.indexed_dataset()
            assert index < len(dataset)
            data = []
            c_index = index

            while len(data) < page_size and c_index < len(dataset):
                if c_index in dataset:
                      data.append(dataset[c_index])
                c_index += 1

            if c_index < len(dataset):
                 next_index = c_index
            else:
                 next_index = None

            return {
                 'index': index,
                 'next_index': next_index,
                 'page_size': len(data),
                 'data': data
            }
