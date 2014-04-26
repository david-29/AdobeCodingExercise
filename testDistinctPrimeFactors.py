import unittest
import distinctPrimeFactors


class TestDistinctPrimeFactors(unittest.TestCase):
    """Unit test for the distinctPrimeFactors module"""

    def test_get_number_letter_count_for_range(self):
        self.assertEqual(14, distinctPrimeFactors.find_n_consecutive_numbers_with_n_distinct_prime_factors(2))
        self.assertEqual(644, distinctPrimeFactors.find_n_consecutive_numbers_with_n_distinct_prime_factors(3))


# Run the unit tests
unittest.main()
