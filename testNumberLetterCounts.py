import unittest
import numberLetterCounts


class TestNumberLetterCounts(unittest.TestCase):
    """Unit test for the numberLetterCounts module"""

    def test_get_number_letter_count_for_range(self):
        self.assertEqual(3, numberLetterCounts.get_number_letter_count_for_range(1, 1))
        self.assertEqual(39, numberLetterCounts.get_number_letter_count_for_range(1, 10))
        self.assertEqual(161, numberLetterCounts.get_number_letter_count_for_range(1, 25))
        self.assertEqual(124, numberLetterCounts.get_number_letter_count_for_range(8, 24))
        self.assertEqual(190, numberLetterCounts.get_number_letter_count_for_range(90, 105))
        self.assertEqual(20, numberLetterCounts.get_number_letter_count_for_range(115, 115))
        self.assertEqual(23, numberLetterCounts.get_number_letter_count_for_range(342, 342))
        self.assertEqual(643, numberLetterCounts.get_number_letter_count_for_range(495, 525))
        self.assertEqual(311, numberLetterCounts.get_number_letter_count_for_range(995, 1010))


# Run the unit tests
unittest.main()


