import manipulation_histogramme.py as mh
import unittest
import numpy as np

def test_calculer_histogramme():
    assert mh.calculer_histogramme(np.array([225, 160, 10, 49, 20, 170, 1, 121, 30, 223, 230, 100, 255, 23, 155, 88]), 3) == np.array([4, 0, 2, 3, 3, 2, 2, 2, 4, 0, 2, 3, 2, 3, 2, 2])
    
def test_calculer_distance_1():
    assert mh.calculer_distance_1(np.array([1, 2, 3, 4, 5]), np.array([2, 3, 4, 5, 6])) == 2.24

def test_calculer_distance_2():
    assert mh.calculer_distance_2(np.array([1, 2, 3, 4, 5]), np.array([2, 3, 4, 5, 6])) == 5

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
