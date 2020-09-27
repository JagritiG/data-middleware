"""
Author: Jagriti Goswami
Date: 31th August 2020
License: MIT License
==================================================================================
Implementation of merge sort algorithm in Python
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves,
calls itself for the two halves and then merges the two sorted halves.

param nums: list of n elements to sort
return: sorted list (in ascending order)

Examples:
merge_sort([]) # output :[]
merge_sort([5, 2, 4, 2])   # output: [2, 2, 4, 5]
merge_sort([5, -3, 4, -5])   # output: [-5, -3, 4, 5]

Time complexity:
Worst-case 	O(nlogn)
Best-case O(nlogn) typical, O(n) natural variant
Average O(nlogn)
Space complexity: O(n) total with O(n) auxiliary,
O(1) auxiliary with linked list
"""
# ================================================================================
import inspect
import heapq


# Merge-Sort
def merge_sort(nums: list) -> list:
    """ It divides input array in two halves, calls itself
    for the two halves and then merges the two sorted halves.

    :param nums: list of n elements to sort
    :return: sorted list (in ascending order)
    """

    if type(nums) is not list:
        raise TypeError("merge sort only takes lists, not {}".format(str(type(nums))))

    try:
        if len(nums) > 1:
            mid = len(nums) // 2
            left_list = nums[:mid]
            right_list = nums[mid:]

            # Recursively breakdown the list
            merge_sort(left_list)
            merge_sort(right_list)

            # Perform the merging
            i = 0 # index into the left_list
            j = 0 # index into the right_list
            k = 0 # index into the merge list

            # While both lists have content
            while i < len(left_list) and j < len(right_list):
                if left_list[i] < right_list[j]:
                    nums[k] = left_list[i]
                    i += 1
                else:
                    nums[k] = right_list[j]
                    j += 1
                k += 1

            # If the left_list still has values, add them
            while i < len(left_list):
                nums[k] = left_list[i]
                i += 1
                k += 1

            # If the right_list still has values, add them
            while j < len(right_list):
                nums[k] = right_list[j]
                j += 1
                k += 1

        return nums

    except TypeError:
        return []


# ==================================================================================
# Implementation of quick sort algorithm in Python
# Quick Sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element
# from the array and partitioning the other elements into two sub-arrays,
# according to whether they are less than or greater than the pivot.
# The sub-arrays are then sorted recursively. This can be done in-place, requiring small
# additional amounts of memory to perform the sorting.
#
# param nums: list of n elements to sort
# return: sorted list (in ascending order)
#
# Examples:
# quick_sort([]) # output :[]
# quick_sort([5, 2, 4, 2])   # output: [2, 2, 4, 5]
# quick_sort([5, -3, 4, -5])   # output: [-5, -3, 4, 5]
#
# Time complexity:
# Worst-case 	O(n2)
# Best-case O(nlogn)
# Average O(nlogn)
# Space complexity: O(n) auxiliary (naive),
# O(nlogn) auxiliary
# ================================================================================

# Quick-Sort
def quick_sort(nums: list) -> list:
    """ Selects an element as pivot and partitions the given array around this pivot.
    The sub-arrays are then sorted recursively.

    :param nums: list of n elements to sort
    :return: sorted list (in ascending order)
    """

    if type(nums) is not list:
        raise TypeError("quick sort only takes lists, not {}".format(str(type(nums))))

    length = len(nums)
    try:

        if length <= 1:
            return nums
        else:
            # Use the last element as the first pivot
            pivot = nums.pop()
            # Put elements greater than pivot in right list
            # Put elements lesser than pivot in left list
            right, left = [], []
            for num in nums:
                if num > pivot:
                    right.append(num)
                else:
                    left.append(num)
            return quick_sort(left) + [pivot] + quick_sort(right)

    except TypeError:
        return []


# ==================================================================================
# Implementation of heap sort algorithm in Python
# Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves,
# calls itself for the two halves and then merges the two sorted halves.
#
# param nums: iterable list of n elements to sort
# return: sorted list (in ascending order)
#
# Examples:
# heap_sort([]) # output :[]
# heap_sort([5, 2, 4, 2])   # output: [2, 2, 4, 5]
# heap_sort([5, -3, 4, -5])   # output: [-5, -3, 4, 5]
#
# Time complexity:
# Worst-case 	O(nlogn)
# Best-case O(nlogn) distict keys, O(n) equal keys
# Average O(nlogn)
# Space complexity: O(n) total with O(1) auxiliary
# ================================================================================


class MinHeap:

    # Create a heap
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.heap)

    # Inserting into heap
    def insert(self, val):
        heapq.heappush(self.heap, val)

    # Size of heap
    def size(self):
        return len(self.heap)

    # Removing element from min heap
    def remove(self):
        return heapq.heappop(self.heap)


# Heap-Sort
def heap_sort(nums: list) -> list:
    """ A heap sort can be implemented by pushing all values onto a heap
    and then popping off the smallest values one at a time.

    :param nums: iterable list of n elements to sort
    :return: sorted list (in ascending order)
    """

    if type(nums) is not list:
        raise TypeError("heap sort only takes lists, not {}".format(str(type(nums))))

    try:
        h = MinHeap()
        array_sorted = []
        for val in nums:
            h.insert(val)
        while h.size() > 0:
            array_sorted.append(h.remove())
        return array_sorted

    except TypeError:
        return []


def source_code(func):
    """
    Return the source code of the function.
    :return: source code
    """
    if func == "merge_sort":
        return inspect.getsource(merge_sort)
    if func == "quick_sort":
        return inspect.getsource(quick_sort)
    if func == "heap_sort":
        return inspect.getsource(heap_sort)


if __name__ == "__main__":

    min_heap = MinHeap()
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(merge_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(quick_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
