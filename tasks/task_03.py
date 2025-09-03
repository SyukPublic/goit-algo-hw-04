# -*- coding: utf-8 -*-

"""
HomeWork Task 3
"""

import timeit
import numpy as np


def insertion_sort(dataset: list[int]) -> list[int]:
    """ Return new sorted list of integers by Insertion Sort implementation

    :param dataset: unsorted list of integers (list of integers, mandatory)
    :return: sorted list of integers (list of integers)
    """

    dataset_sorted: list[int] = dataset[:]
    for i in range(1, len(dataset_sorted)):
        key = dataset_sorted[i]
        j = i-1
        while j >=0 and key < dataset_sorted[j] :
                dataset_sorted[j+1] = dataset_sorted[j]
                j -= 1
        dataset_sorted[j+1] = key
    return dataset_sorted


def merge_sort(dataset: list[int]) -> list[int]:
    """ Return new sorted list of integers by Merge Sort implementation

    :param dataset: unsorted list of integers (list of integers, mandatory)
    :return: sorted list of integers (list of integers)
    """

    def merge(left: list[int], right: list[int]) -> list[int]:
        merged: list[int] = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    if len(dataset) <= 1:
        return dataset[:]

    mid = len(dataset) // 2
    return merge(merge_sort(dataset[:mid]), merge_sort(dataset[mid:]))


def merge_sort_by_numpy(dataset: list[int]) -> list[int]:
    """ Return new sorted list of integers by Merge Sort NumPy implementation

    :param dataset: unsorted list of integers (list of integers, mandatory)
    :return: sorted list of integers (list of integers)
    """

    dataset_np = np.array(dataset)
    dataset_np.sort(kind='mergesort')
    return dataset_np.tolist()


def timsort_by_sorted(dataset: list[int]) -> list[int]:
    """ Return new sorted list of integers by sorted() Timsort implementation

    :param dataset: unsorted list of integers (list of integers, mandatory)
    :return: sorted list of integers (list of integers)
    """
    return sorted(dataset)


def timsort_by_sort(dataset: list[int]) -> list[int]:
    """ Return new sorted list of integers by list.sort() Timsort implementation

    :param dataset: unsorted list of integers (list of integers, mandatory)
    :return: sorted list of integers (list of integers)
    """

    dataset_sorted: list[int] = dataset[:]
    dataset_sorted.sort()
    return dataset_sorted


def sort_algorithms_compare() -> None:

    algorithms: tuple = (
        ("Insertion sort", insertion_sort),
        ("Merge sort", merge_sort),
        ("Merge sort by numpy", merge_sort_by_numpy),
        ("Timsort by sorted()", timsort_by_sorted),
        ("Timsort by list.sort()", timsort_by_sort),
    )

    datasets: list[tuple[str, list[int]]] = [
        (f"List of {size:,} integers", np.random.randint(1, 1001, size=size).tolist(), )
        for size in sorted([100, 1_000, 10_000, 100_000])
    ]

    sort_times: dict[str, dict[str, float]] = {}
    for algorith_name, sort_func in algorithms:
        times: dict[str, float] = {}
        for name, dataset in datasets:
            times[name] = timeit.timeit(lambda: sort_func(dataset), number=5)
        sort_times[algorith_name] = times

    data_max_len = max([len(n) for n, _ in datasets])
    algo_max_len = max([len(n) for n in sort_times.keys()])
    print("|", " | ".join([f"{'Algorithm':<{algo_max_len}}"] + [f"{n:<{data_max_len}}" for n, _ in datasets]), "|")
    print("|", " | ".join(["-"*algo_max_len] + ["-"*data_max_len for _ in datasets]), "|")
    for func, times in sort_times.items():
        print(
            "|",
            " | ".join([f"{func:<{algo_max_len}}"] + [f"{times.get(n, 0):<{data_max_len}.08f}" for n, _ in datasets]),
            "|"
        )
