# Create a function to make a blank grid (just dots)
def initial_grid(rows=10, cols=10):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    return grid

# Include this 2nd function to visualise the blank grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Want to see what the previous 2 functions did.  Plus, personalise the presentation a bit.
grid = initial_grid()
print('The Pyladies\' Slither Sisters present: ')
print_grid(grid)
print('Welcome to our version of Snake!')





