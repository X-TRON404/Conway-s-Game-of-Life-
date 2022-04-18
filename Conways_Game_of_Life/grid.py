
from cell import Cell

class Grid:	
    def __init__(self, m_rows, n_columns):
        '''
        Initialize a grid with m_rows and n_columns with each cell as an instance of the class Cell
        '''
        # Raise error if rows/columns are not integers
        if type(m_rows) != int or type(n_columns) != int:
            raise TypeError('Grid dimensions must be integers')
        self.rows = m_rows
        self.columns = n_columns
        self.grid_array = [[Cell() for column in range(n_columns)] for row in range(m_rows)]
        
    def show_grid(self):
        '''
        Print the 2D grid in the terminal 
        '''
        for row in range(self.rows):
            for column in range(self.columns):
                print('1' if self.grid_array[row][column].is_ON() else '0', end=' ')
            print('')

    def show_cell_neighbours(self, cell_row, cell_column):
        '''
        Print the neighbouring cells for the current cell in mth row and nth column
        '''
        for row in range(cell_row - 1, cell_row + 2):
            # Skip current 'row' if row number is out of bounds
            if row < 0 or row >= self.rows:
                continue
            for column in range(cell_column - 1, cell_column + 2):
                # Skip current 'column' if column number is out of bounds
                if column < 0 or column >= self.columns:
                    continue
                print(row, column, '1' if self.grid_array[row][column].is_ON() else '0', end='-')
            print('')
            
    def check_ON_cell_neighbours(self, cell_row, cell_column):
        '''
        Count and return the neighbouring cells for the current cell in mth row and nth column for the ON status
        '''
        ON_count = 0
        for row in range(cell_row - 1, cell_row + 2):
            # Skip current 'row' if row number is out of bounds
            if row < 0 or row >= self.rows:
                continue
            for column in range(cell_column - 1, cell_column + 2):
                # Skip current 'column' if column number is out of bounds
                if column < 0 or column >= self.columns:
                    continue
                # Skip cell whose neighbours are being checked for
                elif row == cell_row and column == cell_column:
                    continue
                elif self.grid_array[row][column].is_ON():
                    ON_count += 1
        return ON_count