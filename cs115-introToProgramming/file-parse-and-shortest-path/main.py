# Name: Brooke Hughes
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

def parse_file(filename):
    '''
    Takes file with a row and col value and a grid of row rows and col columns 
    Converts file into the grid as a 2D list
    Raises a Value Error if dimensions at the top of the file are inaccurate or don't exist
    Returns the grid as a 2D list
    '''
    # Opens file and initalizes helper variables
    file = open(filename, 'r')
    str_grid = []
    int_grid = []

    # Creates a 2D list of each row in the file, but all numbers are strings
    for line in file:
        str_grid += [line.split()]
    # Creates a new 2D list from the first one, but all numbers are integers
    for row in str_grid:
        int_grid += [list(map(int, row))]
    # Assigns the dimensions of the grid to the first line in the file
    dimensions = int_grid[0]
    int_grid = int_grid[1:]

    # Raises a Value Error if the dimensions at the top of the file are not 2 numbers
    if len(dimensions) != 2:
        raise ValueError("Accurate dimensions not listed at top of file!")
    # Raises a Value Error if the number of columns isn't the same as what's stated in the dimensions
    for row in int_grid:
        if dimensions[0] != len(row):
            raise ValueError("Number of items in at least one row(s) is not equal to dimensions.")
    # Raises a Value Error if the number of rows isn't the same as what's stated in the dimensions
    if len(int_grid) != dimensions[1]:
        raise ValueError("Number of rows is not equal to dimensions.")
    # Returns the grid if all is well
    return int_grid



def distances_from(grid):
    '''
    Takes a grid of costs
    Outputs a 2D list of shortest distances from each block (x, y) in the grid.
    '''
    # initializes number of rows and cols in grid
    rows = len(grid)
    cols = len(grid[0])

    if rows == 0:
        return []
    
    # create dist grid same size as grid
    dists = [[0] * cols for _ in range(rows)]

    # fill (0, 0)
    dists[0][0] = grid[0][0]

    # fill first row
    for i in range(1, cols):
        dists[0][i] = dists[0][i-1] + grid[0][i]
    
    # fill first col
    for j in range(1, rows):
        dists[j][0] = dists[j-1][0] + grid[j][0]
    
    # fill remaining entries
    for i in range(1, rows):
        for j in range(1, cols):
            best = min(dists[i][j-1], dists[i-1][j])
            dists[i][j] = best + grid[i][j]
    
    return dists

def shortest_path(dists, point):
    '''
    Takes a grid of distances and a point
    Returns a list of points on the shortest path from the start to that point
    '''
    # Initalizes loop variables
    x, y = point
    path = []

    while True:
        path.append((x, y))
        if x == 0 and y == 0:
            break

        can_left = x > 0
        can_up = y > 0

        if can_left and can_up:
            if dists[y-1][x] <= dists[y][x-1]:
                y -= 1
            else:
                x -= 1
        elif can_up:
            y -= 1
        else:
            x -= 1
    
    return path

