import hw3 
import unittest

class TestCases(unittest.TestCase):
    def assert_deep_copied(self, x, y):
        self.assertEqual(x, y,
                "Matrix wasn't copied correctly!")
        self.assertFalse(x is y,
                "Matrix has not been deep copied!")
        if len(x) > 0:
            self.assertFalse(x[0] is y[0],
                    "A row has not been deep copied!")
            self.assert_deep_copied(x[1:], y[1:])

    def assert_disjoint_rows(self, A):
        def _adr(B):
            def __adr(C):
                if len(C) == 0:
                    return
                self.assertFalse(B[0] is C[0],
                        "Two rows of matrix are not disjoint!")
                __adr(C[1:])
            if len(B) == 0:
                return
            __adr(B[1:])
        _adr(A)

    def test_empty_case_1(self):
        self.assertEqual(hw3.empty(1,1), [[0]])

    def test_empty_case_2(self):
        self.assertEqual(hw3.empty(3,0), [[],[],[]])

    def test_empty_case_3(self):
        self.assertEqual(hw3.empty(2,2), [[0,0],[0,0]])

    def test_empty_case_4(self):
        self.assert_disjoint_rows(hw3.empty(4,4))

    def test_copy_case_1(self):
        grid = [[1]]
        self.assertEqual(hw3.copy(grid), grid)

    def test_copy_case_2(self):
        grid = [[1,2,3],[1,2,3],[1,2,3]]
        self.assertEqual(hw3.copy(grid), grid)

    def test_copy_case_3(self):
        grid = [[],[],[],[],[]]
        self.assertEqual(hw3.copy(grid), grid)

    def test_copy_case_4(self):
        grid = [[1,0],[0,2]]
        self.assert_deep_copied(hw3.copy(grid), grid)

    def test_increase_row_case_1(self):
        grid = [[1,0],[0,2]]
        hw3.increase_row(grid, 0, 1)
        self.assertEqual(grid, [[2,1],[0,2]])

    def test_increase_row_case_2(self):
        grid = [[5,10,15],[20,25,30],[35,40,45]]
        hw3.increase_row(grid, 2, 100)
        self.assertEqual(grid, [[5,10,15],[20,25,30],[135,140,145]])

    def test_increase_row_case_3(self):
        grid = [[0]]
        hw3.increase_row(grid, 0, 25)
        self.assertEqual(grid, [[25]])

    def test_increase_row_case_4(self):
        grid = [[15,25],[40,60]]
        hw3.increase_row(grid, 1, 25)
        self.assertEqual(grid, [[15,25],[65,85]])

    def test_increase_col_case_1(self):
        grid = [[1,0],[0,2]]
        hw3.increase_col(grid, 0, 1)
        self.assertEqual(grid, [[2,0],[1,2]])

    def test_increase_col_case_2(self):
        grid = [[5,10,15],[20,25,30],[35,40,45]]
        hw3.increase_col(grid, 2, 100)
        self.assertEqual(grid, [[5,10,115],[20,25,130],[35,40,145]])

    def test_increase_col_case_3(self):
        grid = [[0]]
        hw3.increase_col(grid, 0, 25)
        self.assertEqual(grid, [[25]])

    def test_increase_col_case_4(self):
        grid = [[15,25],[40,60]]
        hw3.increase_col(grid, 1, 25)
        self.assertEqual(grid, [[15,50],[40,85]])

    def test_distance_from_case_1(self):
        grid = [[1,5,3],[9,4,7],[2,8,6]]
        self.assertEqual(hw3.distance_from(grid, 2, 2), 22)

    def test_distance_from_case_2(self):
        grid = [[1,5,3],[9,4,7],[2,8,6]]
        self.assertEqual(hw3.distance_from(grid, 2, 0), 12)

    def test_distance_from_case_3(self):
        grid = [[0,0,1,1],
                [1,0,0,0],
                [1,0,1,0],
                [1,0,1,0]]
        self.assertEqual(hw3.distance_from(grid, 3, 3), 0)

    def test_distance_from_case_4(self):
        grid = [[0,0,1,1],
                [1,0,0,0],
                [1,0,1,0],
                [1,0,1,0]]
        self.assertEqual(hw3.distance_from(grid, 3, 2), 1)

    def test_distance_from_case_5(self):
        grid = [[0,0,1,1],
                [1,0,0,0],
                [1,0,1,0],
                [1,0,1,0]]
        self.assertEqual(hw3.distance_from(grid, 3, 2), 1)
        self.assertEqual(grid,
                [[0,0,1,1],
                 [1,0,0,0],
                 [1,0,1,0],
                 [1,0,1,0]],
                "distance_from mutated grid!")

    def test_distance_from_case_6(self):
        grid = [[1,1,1,1,1],
                [100,100,100,100,1],
                [1,1,1,1,1],
                [1,100,100,100,100],
                [1,1,1,1,1]]
        self.assertEqual(hw3.distance_from(grid, 4, 4), 108)

    def test_distance_from_case_7(self):
        grid = [[1,1,1,1,1],
                [100,100,100,100,1],
                [1,1,1,1,1],
                [1,100,100,100,100],
                [1,1,1,1,1]]
        self.assertEqual(hw3.distance_from(grid, 2, 0), 102)

    def test_distance_from_case_8(self):
        grid = [[1,1,1,1,1],
                [100,100,100,100,1],
                [1,1,1,1,1],
                [1,100,100,100,100],
                [1,1,1,1,1]]
        self.assertEqual(hw3.distance_from(grid, 3, 3), 205)

if __name__ == "__main__":
    unittest.main()
