#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.
"""

import csv
from typing import Dict, List, Optional


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """
        Initialize the server caches for dataset and indexed dataset.
        """
        self.__dataset: List[List[str]] = None
        self.__indexed_dataset: Dict[int, List[str]] = None

    def dataset(self) -> List[List[str]]:
        """
        Load and cache the CSV dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """
        Return the dataset indexed by original row position.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                index: dataset[index] for index in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: Optional[int] = None, page_size: int = 10
    ) -> Dict[str, object]:
        """
        Return a deletion-resilient page starting from the given index.
        """
        if index is None:
            index = 0

        indexed_dataset = self.indexed_dataset()
        assert isinstance(index, int) and index >= 0 and index < len(indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0

        data: List[List[str]] = []
        current_index: int = index
        max_index: int = max(indexed_dataset.keys())

        while current_index <= max_index and len(data) < page_size:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        if current_index > max_index:
            current_index = None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current_index,
        }
