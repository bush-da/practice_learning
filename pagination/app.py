#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
from flask import Flask, render_template, request, abort
import csv
import math
from typing import List, Dict


app = Flask(__name__)


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
        """function that return a dictionary"""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)

        if index > total_items:
            raise AssertionError("Index out of range")

        current_index = index
        data = []
        while (len(data) < page_size and current_index < total_items):
            item = indexed_data.get(current_index)

            if item:
                data.append(item)
            current_index += 1

        next_index = current_index if current_index < total_items else None
        return {'index': index, 'next_index': next_index,
                'page_size': page_size, 'data': data}


server = Server()
@app.route('/')
def index():
    try:
        page_index = int(request.args.get('index', 0))
        page_size = int(request.args.get('page_size', 10))
    except ValueError:
        abort(400, 'Invalid page or page size')

    try:
        pagination_data = server.get_hyper_index(page_index, page_size)
    except AssertionError:
        page_index = max(0, len(server.indexed_dataset()) - page_size)
        pagination_data = server.get_hyper_index(page_index, page_size)

    return render_template(
        'index.html',
        data=pagination_data.get('data'),
        index=page_index,
        next_index=pagination_data['next_index'],
        page_size=page_size
    )

if __name__ == '__main__':
    app.run(debug=True)
