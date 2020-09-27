import unittest

from datamidware.pyalgo import search


class TestSearchAlgorithm(unittest.TestCase):
    def setUp(self):
        # to test numeric numbers
        self.arr = list(range(10))

        # to test alphabets
        string = "python"
        self.alphaarr = list(string)


class TestBinarySearch(TestSearchAlgorithm):

    def test_binary_search(self):
        self.assertIs(search.binary_search(self.arr, 9), 9)
        self.assertIs(search.binary_search(self.alphaarr, 't'), 2)
        self.assertIs(search.binary_search(self.arr, 't'), -1)


# class TestLinearSearch(TestSearchAlgorithm):
#
#     def test_linear_search(self):
#         self.assertIs(linear_search.linear_search(self.arr, 9), 9)
#         self.assertIs(linear_search.linear_search(self.alphaarr, 't'), 2)
#         self.assertIs(linear_search.linear_search(self.arr, 't'), -1)


# Test Runner
if __name__ == '__main__':
    unittest.main()
