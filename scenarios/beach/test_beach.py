import unittest
import beach as be

class TestFreeSpaces(unittest.TestCase):

    def test_not_enough_sits(self):
        """
        Test the code if there is not enough sits on the beach to fit everyone
        """
        self.assertEqual(be.checkSpace(['T', 'F', 'F', 'T', 'F', 'F', 'F','T', 'F'], 5), False)

    def test_enough_sits(self):
        """
        Test the code if there is enough sits on the beach to fit everyone
        """
        self.assertEqual(be.checkSpace(['T', 'F', 'F', 'T', 'F', 'F', 'F','T', 'F'], 3), True)

if __name__ == '__main__':
    unittest.main()