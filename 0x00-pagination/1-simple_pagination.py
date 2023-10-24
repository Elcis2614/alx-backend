#!/usr/bin/env python3
"""
    Simple pagination
"""

import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Given the page number and page size,
        The function returns the start and end indexes
        as a tuple
    """
    start = page_size * (page - 1)
    return (start, start + page_size)


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
            takes two integer arguments page with default value 1
            and page_size with default value 10.
            Uses index_range to find the correct indexes to paginate
            the dataset correctly
            and return the appropriate page of the dataset (i.e. the
            correct list of rows).
        """
        assert type(page) == type(page_size) == int
        assert page > 0
        assert page_size > 0
        indexes = index_range(page, page_size)

        if indexes[0] > indexes[1]:
            return []

        if (self.__dataset is None):
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = []
                next(reader)
                try:
                    for i in range(indexes[0]):
                        next(reader)
                    for j in range(indexes[1] - indexes[0]):
                        dataset.append(next(reader))
                except StopIteration:
                    return []
                return dataset
        else:
            length = len(self.__dataset)
            if indexes[0] >= length or indexes[1] >= lenght:
                return []
            return self.__dataset[indexes[0]: indexes[1]]
