import unittest
import airport as ap

class TestAirport(unittest.TestCase):

    def test_standard(self):
        """
        Test standard input
        """
        input = [5, 9, 13, 2, 7, 11, 5, 1, 8, 4, 10, 2, 4, 21, 7, 4, 6, 12, 2]
        plane = ap.Plane(input)
        plane.removeWrongBags()     
        expected_output = [2, 12, 6, 4, 7, 21, 4, 2, 10, 4, 8, 1, 5, 11, 7, 2, 13, 9, 5]
        plane.loadBagsToConatainers()
        output = plane.unloadPlane()

        self.assertEqual(output, expected_output)

    def test_incorrect_bags(self):
        """
        Test standard input
        """
        input = [5, 9, 13, 2, 7, 11, 5, 1, 8, 4, 0, 10, 2, 4, 21, 7, 4, 44, 6, 12, 2]
        plane = ap.Plane(input)
        plane.removeWrongBags()     
        expected_output = [2, 12, 6, 4, 7, 21, 4, 2, 10, 4, 8, 1, 5, 11, 7, 2, 13, 9, 5]
        plane.loadBagsToConatainers()
        output = plane.unloadPlane()

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()