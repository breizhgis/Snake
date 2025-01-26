def initial_grid(rows=10, cols=10):
    # Initialize the grid with dots
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

grid = initial_grid()
print('The Pyladies\' Slither Sisters present: ')
print_grid(grid)
print('Welcome to our version of Snake!')





