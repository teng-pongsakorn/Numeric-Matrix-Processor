import unittest
from . import processor


class MyTestCase(unittest.TestCase):

    def test_get_adjacent(self):
        A = [[2,-1,0],
             [0,1,2],
             [1,1,0]]
        r, c = 0, 0
        expect = -2
        self.assertEqual(expect, processor.get_adjacent(A, r, c))

        r, c = 0, 1
        expect = 2
        self.assertEqual(expect, processor.get_adjacent(A, r, c))

        r, c = 1, 0
        expect = 0
        self.assertEqual(expect, processor.get_adjacent(A, r, c))

        r, c = 1, 1
        expect = 0
        self.assertEqual(expect, processor.get_adjacent(A, r, c))

        r, c = 2, 2
        expect = 2
        self.assertEqual(expect, processor.get_adjacent(A, r, c))

        r, c = 1, 2
        expect = -3
        self.assertEqual(expect, processor.get_adjacent(A, r, c))

    def test_get_adjacent_matrix(self):
        A = [[2, -1, 0],
             [0, 1, 2],
             [1, 1, 0]]
        expect = [[-2,2,-1], [0,0,-3],[-2,-4,2]]
        self.assertEqual(expect, processor.get_adjacent_matrix(A))

    def test_matrix_inverse(self):
        A = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        self.assertEqual(A, processor.inverse_matrix(A))

        A = [[2,-1,0],[0,1,2],[1,1,0]]
        expect = [[0.33, 0, 0.33], [-.33, 0, .66], [.16, .5, -.33]]
        self.assertEqual(expect, processor.inverse_matrix(A))


if __name__ == '__main__':
    unittest.main()
