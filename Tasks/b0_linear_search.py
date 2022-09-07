"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    print(arr)
    idx_min = 0
    val_min = arr[0]
    for idx, val in enumerate(arr[1::]):
        if val < val_min:
            val_min = val
            idx_min = idx +1
        print((idx_min, val_min))
    return val_min
