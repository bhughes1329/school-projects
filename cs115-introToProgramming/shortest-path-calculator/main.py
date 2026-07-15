# === CS 115 Homework 3 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Brooke Hughes
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 3 ===
def empty(m, n):
    '''
    Creates and returns an empty grid with m rows and n columns
        Args:
            m (int): number of rows 
            n (int): number of columns
        Returns: 
            (list): grid with m rows and n columns filled with 0s
    '''
    if m == 0:
        return []
    return [[0] * n] + empty(m - 1, n)

def copy(grid):
    '''
    Returns a deep copy of the given list
        Args:
            grid (list): original matrix
        Returns: 
            (list): deep copy of original matrix
    '''
    return list(map(lambda row: row[:], grid))


def increase_row(grid, y, cost):
    '''
    Increases the cost of all cells in a given row within the grid
        Args:
            grid (list): original matrix
            y (int): row number
            cost (int): amount that row should be increased
        Returns: 
            none (mutates original list)
    '''
    grid[y] = list(map(lambda x: x + cost, grid[y]))

def increase_col(grid, x, cost):
    '''
    Increases the cost of all cells in a given cplumn within the grid
        Args:
            grid (list): original matrix
            x (int): column number
            cost (int): amount that row should be increased
        Returns: 
            none (mutates original list)
    '''
    if grid == []:
        return 
    else:
        grid[0][x] += cost
        increase_col(grid[1:], x, cost)


def distance_from(grid, x, y):
    '''
    Returns the smallest cost that could be incured traveling from the given point to 
    (0, 0) in the given grid
        Args:
            grid (list): matrix of costs
            x (int): x coord
            y (int): y coord
        Returns: 
            minimum cost to travel to (0, 0) in the grid only going left or up
    '''
    grid_memo = {}

    def dist_from(x, y):
        if x < 0 or y < 0:
            return float('inf')
        if x == 0 and y == 0:
            return grid[0][0]
        
        if (x, y) in grid_memo:
            return grid_memo[(x, y)]
        
        up = grid[x][y] + dist_from(x-1, y)
        left = grid[x][y] + dist_from(x, y-1)

        min_route = min(up, left)
        grid_memo[(x, y)] = min_route
        return min_route
    
    return dist_from(x, y)
