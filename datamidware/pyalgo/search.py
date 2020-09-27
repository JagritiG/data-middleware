"""
Author: Jagriti Goswami
Date: 30th August 2020
License: MIT License
===================================================================
Implementation of binary search algorithm in Python

param nums: sorted list (in ascending order) of n integer elements
param target: value to search in nums
return: If target exists, then return its index, otherwise return -1.

Examples:
binary_search([0, 3, 5, 10], 3)  # output: 1
binary_search([0, 3, 5, 10], 10) # output: 3
binary_search([0, 3, 5, 10], 11) # output: -1

Time complexity:
Worst-case 	O(log n)
Best-case O(1)
Average O(log n)
Space complexity: O(1)
"""
# ===================================================================
from __future__ import division
import inspect


def binary_search(nums: list, target: int) -> int:
    """Search target value from an sorted list (in ascending order)
    and returns index if target is found. Otherwise return -1.
    """

    if type(nums) is not list:
        raise TypeError("binary search only takes lists, not {}".format(str(type(nums))))

    left = 0
    right = len(nums) - 1

    try:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    except TypeError:
        return -1


def source_code():
    """
    Return the source code of the function.
    :return: source code
    """
    return inspect.getsource(binary_search)

