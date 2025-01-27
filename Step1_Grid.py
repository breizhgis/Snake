# Create a function to make a blank grid (just dots)
def initial_grid(rows=10, cols=10):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    return grid

# Include this function to visualize the blank grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Display the blank grid
grid = initial_grid()
print('The Pyladies\' Slither Sisters present: ')
print_grid(grid)
print('Welcome to our version of Snake!')

# Create a function to make the actual game grid
def game_grid(rows=10, cols=10, snake_body=[]):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]  # Create empty grid
    
    # Loop through each row and column and place 'X' where the snake is
    for row in range(rows):
        for col in range(cols):
            if (row, col) in snake_body:  # Check if the current position is part of the snake body
                grid[row][col] = 'X'  # Mark the snake's body with 'X'
    
    return grid

# Snake body positions (just an example)
snake_body = snake_body = [(0,0), (0,1),(1,0), (2,0), (2,1), (2,2), (2,3), (3,3), (4,3)]

# Display the game grid with the snake
grid = game_grid(snake_body=snake_body)
print("Game Grid with Snake:")
print_grid(grid)
 
    
    


