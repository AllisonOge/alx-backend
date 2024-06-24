#!/usr/bin/env python3
"""2-hypermedia_pagination.py"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """get index range"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


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
        """get the page indexes"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        start_idx = start_idx if start_idx >= 0 else None
        dataset = self.dataset()
        end_idx = end_idx if end_idx < len(dataset) else None
        return [] if start_idx is None or end_idx is None \
            else dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get hypermedia pagination"""
        data = self.get_page(page, page_size)
        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": (page + 1)
                if (page + 1) * page_size <= len(self.dataset()) else None,
                "prev_page": (page - 1) if (page - 1) > 0 else None,
                "total_pages": int(round(len(self.dataset()) / page_size, 0))
                }
