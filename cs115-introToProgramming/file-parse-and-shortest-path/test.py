import unittest
import random
import os
import hw6
import multiprocessing 

class TestParseFile(unittest.TestCase):

    def test_parse_file_valid_example(self):
        grid = hw6.parse_file("grids/example.txt")
        expected = [
            [1, 5, 7, 1],
            [3, 6, 4, 2],
            [7, 2, 3, 5],
        ]
        self.assertEqual(grid, expected)

    def test_parse_file_invalid_missing_dimensions(self):
        """not listing the dimensions at the top of the file should raise a ValueError."""
        with self.assertRaises(ValueError):
            hw6.parse_file("grids/invalid_missing_dimensions.txt")

    def test_parse_file_invalid_wrong_dimension_values(self):
        """listing too few integers should raise a ValueError."""
        with self.assertRaises(ValueError):
            hw6.parse_file("grids/invalid_wrong_dimension_values.txt")

    def test_parse_file_invalid_row_too_short(self):
        """a row containing fewer than m values should raise ValueError"""
        with self.assertRaises(ValueError):
            hw6.parse_file("grids/invalid_row_too_short.txt")

    def test_parse_file_invalid_too_few_rows(self):
        """containing fewer than n rows should raise a ValueError"""
        with self.assertRaises(ValueError):
            hw6.parse_file("grids/invalid_too_few_rows.txt")


class TestDistancesFrom(unittest.TestCase):

    def test_distances_from_simple_grid(self):
        grid = [
            [1, 2, 4],
            [5, 3, 7],
            [10, 5, 6],
        ]

        d = hw6.distances_from(grid)

        expected = [
            [1, 3, 7],
            [6, 6, 13],
            [16, 6+5, 11+6],
        ]

        self.assertEqual(d, expected)

    def test_distances_from_rectangular_grid(self):
        grid = [
            [2, 9, 1, 1],
            [1, 2, 1, 1],
        ]
        d = hw6.distances_from(grid)

        expected = [
            [2, 11, 12, 13],
            [3, 5, 6, 7],
        ]

        self.assertEqual(d, expected)



    def test_efficient_distance_from_15x20_grid_under_one_second(self):
        """distances_from should finish on a 15 x 20 grid in < 1s."""
        grid_path = "grids/grid_15x20.txt"
        grid = hw6.parse_file(grid_path)

        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        p = multiprocessing.Process(
            target=_run_distances, args=(grid, return_dict)
        )
        timeout = 1 # needs to run in < 1 second
        p.start()
        p.join(timeout=timeout)  # ---- 1 second timeout

        if p.is_alive():
            p.terminate()
            self.fail(f"distances_from took longer than 1 second:")

        self.assertIn("ok", return_dict)

    def test_efficient_distance_from_random_medium_grid_under_one_second(self):
        grid = [[random.randint(1,10)]*10 for _ in range(10)]

        path = "grids/tmp_10x10.txt"
        with open(path, "w") as f:
            f.write("10 10\n")
            for row in grid:
                f.write(" ".join(map(str, row)) + "\n")

        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        p = multiprocessing.Process(
            target=_run_distances, args=(path, return_dict)
        )
        p.start()
        p.join(timeout=1.0)

        if p.is_alive():
            p.terminate()
            os.remove(path)
            self.fail("distances_from took longer than 1 second")

        os.remove(path)
        self.assertIn("ok", return_dict)

class TestShortestPath(unittest.TestCase):

    def test_shortest_path_simple_2x2(self):
        dists = [
            [0, 1],
            [1, 2],
        ]
        # path should go (1,1) -> (1,0) -> (0,0) OR
        #                     -> (0,1) -> (0,0)
        result = hw6.shortest_path(dists, (1,1))
        self.assertEqual(result[0], (1,1))
        self.assertEqual(result[-1], (0,0))
        # Multiple potential paaths, so we don't check 1
        self.assertEqual(len(result), 3)

    def test_shortest_path_example_from_handout(self):
        """
        example from the handout
        """
        dists = [
            [1, 6, 13, 14],
            [4, 10, 14, 16],
            [11, 12, 15, 20],
        ]

        expected = [(3,2), (2,2), (1,2), (1,1), (0,1), (0,0)]
        result = hw6.shortest_path(dists, (3,2))
        self.assertEqual(result, expected)

    def test_shortest_path_4x4(self):
        dists = [
            [0, 1, 2, 3],
            [1, 2, 9, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
        ]
        expected = [
            (3,3), (3,2), (3,1), (3,0),
            (2,0), (1,0), (0,0)
        ]
        result = hw6.shortest_path(dists, (3,3))
        self.assertEqual(result, expected)


def _run_distances(grid, return_dict):
    """
    Helper function:
    runs distances from on a sample grid
    fills in return_dict with the key "ok"
    if it runs successfully

    does not check correctness of dists, just efficiency
    """
    try:
        dists = hw6.distances_from(grid)
        return_dict["ok"] = True
    except Exception as e:
        print(e)
        return_dict["error"] = str(e)

if __name__ == "__main__":
    unittest.main()
