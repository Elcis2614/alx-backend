#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List
from typing import Dict


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
            with two integer arguments: index with a None
            default value and page_size with default value of 10.
            The method returns a dictionary with the following key-value pairs:
                index: the current start index of the return page.
                next_index: the next index to query with.
                page_size: the current page size
                data: the actual page of the dataset
        """
        assert 0 <= index < len(self.__indexed_dataset)
        mDict = {"index": index}
        data = []
        count = 0
        new_index = index
        while (len(data) < page_size):
            try:
                value = self.__indexed_dataset[count + index]
                if len(data) == 0:
                    new_index = count + index
                data.append(value)
                count += 1
            except KeyError:
                count += 1
                continue
        mDict["data"] = data
        mDict["next_index"] = new_index + page_size
        mDict["page_size"] = len(data)
        return mDict
