import unittest

from datamidware.pyalgo import sort


class TestMergeSort(unittest.TestCase):

    def test_merge_sort_with_positive_numbers(self):
        self.assertEqual(sort.merge_sort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_merge_sort_negative_numbers(self):
        self.assertEqual(sort.merge_sort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_merge_sort_with_negative_and_positive_numbers(self):
        self.assertEqual(sort.merge_sort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_merge_sort_same_numbers(self):
        self.assertEqual(sort.merge_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_merge_sort_empty_list(self):
        self.assertEqual(sort.merge_sort([]), [])


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_with_positive_numbers(self):
        self.assertEqual(sort.quick_sort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_quick_sort_negative_numbers(self):
        self.assertEqual(sort.quick_sort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_quick_sort_with_negative_and_positive_numbers(self):
        self.assertEqual(sort.quick_sort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_quick_sort_same_numbers(self):
        self.assertEqual(sort.quick_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_quick_sort_empty_list(self):
        self.assertEqual(sort.quick_sort([]), [])


class TestHeapSort(unittest.TestCase):

    def test_heap_sort_with_positive_numbers(self):
        self.assertEqual(sort.heap_sort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_heap_sort_negative_numbers(self):
        self.assertEqual(sort.heap_sort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_heap_sort_with_negative_and_positive_numbers(self):
        self.assertEqual(sort.heap_sort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_heap_sort_same_numbers(self):
        self.assertEqual(sort.heap_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_heap_sort_empty_list(self):
        self.assertEqual(sort.heap_sort([]), [])


# Test Runner
if __name__ == '__main__':
    unittest.main()

