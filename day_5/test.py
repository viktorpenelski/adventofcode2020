import unittest

from day_5.day_5_solution import find_row, find_col, find_id


class TestRows(unittest.TestCase):

    def test_find_row(self):
        self.assertEqual(44, find_row("FBFBBFFRLR"))
        self.assertEqual(70, find_row("BFFFBBFRRR"))
        self.assertEqual(14, find_row("FFFBBBFRRR"))
        self.assertEqual(102, find_row("BBFFBBFRLL"))


class TestCols(unittest.TestCase):

    def test_find_col(self):
        self.assertEqual(5, find_col("FBFBBFFRLR"))
        self.assertEqual(7, find_col("BFFFBBFRRR"))
        self.assertEqual(7, find_col("FFFBBBFRRR"))
        self.assertEqual(4, find_col("BBFFBBFRLL"))


class TestFindId(unittest.TestCase):

    def test_find_id(self):
        self.assertEqual(357, find_id(44, 5))
        self.assertEqual(567, find_id(70, 7))
        self.assertEqual(119, find_id(14, 7))
        self.assertEqual(820, find_id(102, 4))
