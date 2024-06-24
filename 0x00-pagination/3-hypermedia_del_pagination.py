#!/usr/bin/env python3
"""3-hypermedia_del_pagination.py"""
import csv
import math
from typing import List, Dict


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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get hypermedia pagination"""
        assert index is not None and 0 <= index < len(self.indexed_dataset())
        
        next_idx = index
        data = []
        indexed_dataset = self.indexed_dataset()
        
        for i in range(index, index + page_size):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])
            next_idx = i

        return {
                "index": index,
                "next_index": next_idx + 1,
                "page_size": page_size,
                "data": data
                }
