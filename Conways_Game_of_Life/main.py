import json
from game import conways_game
from grid import Grid

with open('./config.json') as json_file:
    config = json.load(json_file)

if __name__ == "__main__":
    timesteps = config['timesteps']
    rows = config['rows']
    columns = config['columns']
    #take input from the user
    input('Welcome to Conways Game of Life.')
    input('You can change the default game settings from the "config.json" file.')
    input(f'Running {rows}*{columns} simulation for {timesteps} timesteps.')
    my_grid = Grid(rows,columns)
    conways_game(my_grid, timesteps)

