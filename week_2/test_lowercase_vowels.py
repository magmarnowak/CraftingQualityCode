import unittest
import lowercase_vowels

class test_lowercase_vowels(unittest.TestCase):
    """Unitest methods for count_lowercase_vowels."""

    def test_lowercase_vowels_1(self):
        """Test count_lowercase_vowels with 'Happy Anniversary!'"""

        actual = lowercase_vowels.count_lowercase_vowels('Happy Anniversary!')
        expected = 4
        self.assertEqual(expected, actual)

    def test_lowercase_vowels_2(self):
        """Test count_lowercase_vowels with 'xyz'"""

        actual = lowercase_vowels.count_lowercase_vowels('xyz')
        expected = 0
        self.assertEqual(expected, actual)

    def test_lowercase_vowels_3(self):
        """ Test count_lowercase_vowels with an empty string """

        actual = lowercase_vowels.count_lowercase_vowels('')
        expected = 0
        self.assertEqual(expected, actual)

    def test_lowercase_vowels_4(self):
        """Test count_lowercase_vowels with a single char, non-consonant"""

        actual = lowercase_vowels.count_lowercase_vowels('c')
        expected = 0
        self.assertEqual(expected, actual)

    def test_lowercase_vowels_5(self):
        """Test count_lowercase_vowels with a single char, vowel"""

        actual = lowercase_vowels.count_lowercase_vowels('a')
        expected = 1
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
