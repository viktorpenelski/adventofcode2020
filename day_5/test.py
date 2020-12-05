import unittest

from day_5 import find_row


class TestRows(unittest.TestCase):

    def test_find_row(self):
        self.assertEqual(44, find_row("FBFBBFFRLR"))
        self.assertEqual(70, find_row("BFFFBBFRRR"))
        self.assertEqual(14, find_row("FFFBBBFRRR"))
        self.assertEqual(102, find_row("BBFFBBFRLL"))
