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

# Create a function to make actual game grid.  Start with code that was already written above.
def game_grid(rows=10, cols=10):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    snake_body = [] # Empty list as coordinates will be defined outside of the function itself

    for row in range(rows):
        for col in range(cols):
            if (row + col) == snake_body:  
                grid[row][col] = 'X'
            else:
                grid[row][col] = '.'
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

grid = game_grid()
snake_body = [(0,0),(1,0),(2,2),(4,3),(8,9),(9,9)]
print_grid(grid)
 
    
    


