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

    def merge(left: list[int], right: list[int]):
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
        return dataset

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

    datasets: tuple = (
        ("List of 1 000 integers", np.random.randint(1, 1001, size=1_000).tolist(), ),
        ("List of 10 000 integers", np.random.randint(1, 1001, size=10_000).tolist(), ),
        ("List of 100 000 integers", np.random.randint(1, 1001, size=100_000).tolist(), ),
        ("List of 1 000 000 integers", np.random.randint(1, 1001, size=1_000_000).tolist(), ),
    )

    algorithms: tuple = (
        ("Insertion sort", insertion_sort),
        ("Merge sort", merge_sort),
        ("Merge sort by numpy", merge_sort_by_numpy),
        ("Timsort by sorted()", timsort_by_sorted),
        ("Timsort by list.sort()", timsort_by_sort),
    )

    sort_times: dict[str, dict[str, float]] = {}
    for algorith_name, sort_func in algorithms:
        times: dict[str, float] = {}
        for name, dataset in datasets:
            times[name] = timeit.timeit(lambda: sort_func(dataset), number=5)
        sort_times[algorith_name] = times

    datasets_max_name_length = max([len(n) for n, _ in datasets])
    algorithms_max_name_length = max([len(n) for n in sort_times.keys()])
    print(
        "| ",
        " | ".join(
            [f"{'Algorithm':<{algorithms_max_name_length}}"]
            +
            [f"{n:<{datasets_max_name_length}}" for n, _ in datasets]
        )
    )
    print("| ", " | ".join(["-"*algorithms_max_name_length] + ["-"*datasets_max_name_length for _ in datasets]))
    for func_name, times in sort_times.items():
        print(
            "| ",
            " | ".join(
                [f"{func_name:<{algorithms_max_name_length}}"]
                +
                [f"{times.get(n, 0):<{datasets_max_name_length}.08f}" for n, _ in datasets]
            )
        )
