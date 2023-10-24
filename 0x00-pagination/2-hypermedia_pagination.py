#!/usr/bin/env python3
"""
    Simple pagination
"""

import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> List[List]:
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
            if indexes[0] >= length or indexes[1] >= length:
                return []
            return self.__dataset[indexes[0]: indexes[1]]

    def get_hyper(self, page: int, page_size: int) -> dict:
        """
            method that takes the same arguments (and defaults) as
            get_page and returns a dictionary of a format:
              page_size: the length of the returned dataset page
              page: the current page number
              data: the dataset page (equivalent to return from previous task)
              next_page: number of the next page, None if no next page
              prev_page: number of the previous page, None if no previous page
              total_pages: the total number of pages in the dataset : integer
        """
        mDict = {}
        data_set = self.get_page(page, page_size)
        mDict["page_size"] = len(data_set)
        mDict["page"] = page
        mDict["data"] = data_set
        if self.get_page(page + 1, page_size) == []:
            mDict["next_page"] = None
        else:
            mDict["next_page"] = page + 1
        if page == 1:
            mDict["prev_page"] = None
        else:
            mDict["prev_page"] = page - 1
        if (self.__dataset is not None):
            mDict["total_pages"] = int(len(self.__dataset) / page_size)
        else:
            mDict["total_pages"] = int(len(self.dataset()) / page_size)
        return mDict
