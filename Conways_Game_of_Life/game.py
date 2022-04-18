import copy
from grid import Grid

def conways_game(grid, timesteps):
    '''
    This function implements the Conway's Game of life for n timesteps and returns the final grid
    '''
    grid = grid
    # If timesteps is not an integer, raise an error
    if type(timesteps) is not int:
        raise TypeError('timesteps must be an integer')
    # If timesteps are negative, raise an error
    if timesteps<0:
        raise ValueError('timesteps must be positive')
    # If timestpes are 0, return the original grid
    if timesteps==0:
        return grid.grid_array
    print('original grid:')
    grid.show_grid()
    # Save original grid as the next grid
    next_grid = copy.deepcopy(grid)
    # Run the game for n timesteps
    for timestep in range(timesteps):
        for row in range(grid.rows):
            for column in range(grid.columns):
                # Check for rules defined by Conway's Game in each timestep:
                # Store number of ON Neighbours for the current cell
                ON_neighbours = grid.check_ON_cell_neighbours(row, column)

                if grid.grid_array[row][column].is_ON():
                    if ON_neighbours < 2 or ON_neighbours > 3:
                        next_grid.grid_array[row][column].turn_OFF()
                    elif ON_neighbours == 2 or ON_neighbours == 3:
                        pass
                    else:
                        pass
                else:
                    if ON_neighbours == 3:
                        next_grid.grid_array[row][column].turn_ON()
        # Copy the next grid to the current grid
        grid = copy.deepcopy(next_grid)
        print(f'{timestep+1}th timestep:')
        grid.show_grid()
    return grid
