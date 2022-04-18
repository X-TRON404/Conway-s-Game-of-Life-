import unittest
from game import conways_game
from grid import Grid
from cell import Cell

class TestCell(unittest.TestCase):
    def test_value_conways_game(self):
        '''This test will fail if the output grid_array of the conways_game function is not the same as the expected grid_array'''
        # Test with a grid of size 3x3 and 0 number of generations 
        test_grid = Grid(3,3)
        test_grid.grid_array = [[Cell(True),Cell(False),Cell(False)],[Cell(False),Cell(True),Cell(False)],[Cell(False),Cell(True),Cell(False)]]
        expected_grid = Grid(3,3)
        expected_grid.grid_array = [[Cell(True),Cell(False),Cell(False)],[Cell(False),Cell(True),Cell(False)],[Cell(False),Cell(True),Cell(False)]]
        conways_game(test_grid, 0)
        for i in range(test_grid.rows):
            for j in range (test_grid.columns):
                self.assertEqual(test_grid.grid_array[i][j].is_ON() , expected_grid.grid_array[i][j].is_ON())

        # Test with a grid of size 3x3 and a number of generations of 1
        test_grid = Grid(3,3)
        test_grid.grid_array = [[Cell(False),Cell(True),Cell(False)],[Cell(False),Cell(True),Cell(True)],[Cell(False),Cell(False),Cell(False)]]
        expected_grid = Grid(3,3)
        expected_grid.grid_array = [[Cell(False),Cell(True),Cell(True)],[Cell(False),Cell(True),Cell(True)],[Cell(False),Cell(False),Cell(False)]]
        test_grid = conways_game(test_grid, 1)
        for i in range(test_grid.rows):
            for j in range (test_grid.columns):
                self.assertEqual(test_grid.grid_array[i][j].is_ON() , expected_grid.grid_array[i][j].is_ON())

        # Test with a grid of size 4x4 and a number of generations of 2
        test_grid = Grid(4,4)
        test_grid.grid_array = [[Cell(True),Cell(False),Cell(False),Cell(True)],[Cell(False),Cell(False),Cell(True),Cell(False)],[Cell(True),Cell(False),Cell(True),Cell(False)],[Cell(False),Cell(True),Cell(True),Cell(False)]]
        expected_grid = Grid(4,4)
        expected_grid.grid_array = [[Cell(False),Cell(False),Cell(False),Cell(False)],[Cell(False),Cell(False),Cell(True),Cell(True)],[Cell(False),Cell(False),Cell(False),Cell(False)],[Cell(False),Cell(True),Cell(True),Cell(True)]]
        test_grid = conways_game(test_grid, 2)
        for i in range(test_grid.rows):
            for j in range (test_grid.columns):
                self.assertEqual(test_grid.grid_array[i][j].is_ON() , expected_grid.grid_array[i][j].is_ON())

if __name__ == '__main__':
    unittest.main()