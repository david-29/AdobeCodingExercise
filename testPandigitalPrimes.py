import unittest
import pandigitalPrimes


class TestPandigitalPrimes(unittest.TestCase):
    """Unit test for the pandigitalPrimes module"""

    def test_find_largest_prime_pandigital(self):
        self.assertEqual(4231, pandigitalPrimes.find_largest_prime_pandigital_number(4))
        self.assertEqual(7652413, pandigitalPrimes.find_largest_prime_pandigital_number(7))


# Run the unit tests
unittest.main()
