import unittest
from cell import Cell
from grid import Grid

class TestGame(unittest.TestCase):
    def test_types_column_row_size(self):
        '''This test will fail if the row/column value is not an integer'''
        my_grid = Grid(3,3)
        self.assertTrue(type(my_grid.columns) is int)
        self.assertTrue(type(my_grid.rows) is int)

    def test_count_check_ON_cell_neighbours(self):
        '''This test will fail if the number of ON neighbours is not counted correctly'''

        # A grid of size 3x3 with a all ON cells
        my_grid = Grid(3,3)
        my_grid.grid_array = [[Cell(True) for column in range(my_grid.rows)] for row in range(my_grid.columns)]
        '''
        Grid:
        |True|True|True|
        |True|True|True|
        |True|True|True|
        '''
        self.assertEqual(my_grid.check_ON_cell_neighbours(0,0), 3)
        self.assertEqual(my_grid.check_ON_cell_neighbours(0,1), 5)
        self.assertEqual(my_grid.check_ON_cell_neighbours(0,2), 3)
        self.assertEqual(my_grid.check_ON_cell_neighbours(1,0), 5)
        self.assertEqual(my_grid.check_ON_cell_neighbours(1,1), 8)
        self.assertEqual(my_grid.check_ON_cell_neighbours(1,2), 5)
        self.assertEqual(my_grid.check_ON_cell_neighbours(2,0), 3)
        self.assertEqual(my_grid.check_ON_cell_neighbours(2,1), 5)
        self.assertEqual(my_grid.check_ON_cell_neighbours(2,2), 3)

        # A grid of size 3x3 with a all OFF cells
        my_grid.grid_array = [[Cell(False) for column in range(my_grid.rows)] for row in range(my_grid.columns)]
        '''
        Grid:
        |False|False|False|
        |False|False|False|
        |False|False|False|
        '''
        self.assertEqual(my_grid.check_ON_cell_neighbours(0,0), 0)
        self.assertEqual(my_grid.check_ON_cell_neighbours(0,1), 0)
        self.assertEqual(my_grid.check_ON_cell_neighbours(0,2), 0)
        self.assertEqual(my_grid.check_ON_cell_neighbours(1,0), 0)
        self.assertEqual(my_grid.check_ON_cell_neighbours(1,1), 0)
        self.assertEqual(my_grid.check_ON_cell_neighbours(1,2), 0)
        self.assertEqual(my_grid.check_ON_cell_neighbours(2,0), 0)
        self.assertEqual(my_grid.check_ON_cell_neighbours(2,1), 0)
        self.assertEqual(my_grid.check_ON_cell_neighbours(2,2), 0)


if __name__ == '__main__':
    unittest.main()






