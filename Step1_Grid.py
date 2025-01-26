# Initialize a 10x10 grid with dots
grid = [['.' for _ in range(10)] for _ in range(10)]

# Replace specific positions with 'X' using nested loops
for row in range(10):
    for col in range(10):
        # Replace dots with 'X' where you want
        if (row + col) % 2 == 0:  # Example: 'X' on every even-index sum
            grid[row][col] = 'X'

# Print the grid
for row in grid:
    print(' '.join(row))





