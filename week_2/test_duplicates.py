import unittest
import duplicates

class TestRemoveShared(unittest.TestCase):
    """Unittest methods for remove_shared."""

    # def test_removeshared_1(self):
    #     """Test remove_shared on empty lists"""
    #
    # def test_removeshared_2(self):
    #     """Test remove_shared on
    def test_general_case(self):
        """
        Test remove_shared where there are items that appear in both lists,
        and items that appear only on one or the pther list.
        """

        list_1 = [1, 2, 3, 4, 5, 6]
        list_2 = [2, 4, 5, 7]
        list_1_expected = [1, 3, 6]
        list_2_expected = [2, 4, 5, 7]

        duplicates.remove_shared(list_1, list_2)
        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)

if __name__ == '__main__':
    unittest.main(exit=False)
