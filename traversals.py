"""Traverses in different patterns"""
# Name: Sanjitha Venkata
# EID: sv28325


def row_major_traversal(grid):
    """Iterates over a 2D list from left to right, then top 
    to bottom and returning the coordinates (row, column)."""
    result=[]
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            result.append((r,c))
    return result
def column_major_traversal(grid):
    """Iterates over a 2D list from left to right, then top to 
    bottom and returning the coordinates (row, column)."""
    result=[]
    rows = len(grid)
    cols = len(grid[0])
    for c in range(cols):
        for r in range(rows):
            result.append((r,c))
    return result


def row_zigzag_traversal(grid):
    """Iterates over a 2D list from top to bottom then left 
    to right and returning the coordinates (row, column)."""
    result=[]
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        if r%2 != 0: #for odd rows, iterate backwards through columns
            for c in range(cols-1,-1,-1):
                result.append((r,c))
        else:
            for c in range(cols):
                result.append((r,c))
    return result
def column_zigzag_traversal(grid):
    """Iterates over a 2D list by alternating between iterating 
    left to right and right to left, going from top to bottom and 
    returning the coordinates (row, column)."""
    result=[]
    rows = len(grid)
    cols = len(grid[0])
    for c in range(cols):
        if c%2 != 0: #for odd cols, iterate backwords through rows
            for r in range(rows-1,-1,-1):
                result.append((r,c))
        else:
            for r in range(rows):
                result.append((r,c))
    return result


def main_diagonal_traversal(grid):
    """Iterates over a 2D list from the top-right to the bottom-left
    in the direction of the main diagonal and returning the coordinates 
    (row, column)."""
    result = []
    rows = len(grid)
    cols = len(grid[0])

    #moving through columns from right to left one by one
    for c in range(cols-1, -1, -1):
        r = 0 #stays this way for all of the top diagonals that dont hit the left column yet
        while r < rows and c < cols: #if in range of grid, adds all r+1 and c+1 to list
            result.append((r, c))
            r += 1
            c += 1
    for r in range(1, rows): #once done w top diagonals, switches to first column second row
        c = 0 #stays starting from first col
        while r < rows and c < cols: #while in range of grid, adds all diagonals to list
            result.append((r, c))
            r += 1
            c += 1
    return result
def secondary_diagonal_traversal(grid):
    """Iterates over a 2D list from the top-left to the bottom-right in 
    the direction of the secondary diagonal and returning the coordinates (row, column)."""
    result = []
    rows = len(grid)
    cols = len(grid[0])

    for c in range(cols):
        r = 0
        while r<rows and c>=0 :
            result.append((r, c))
            r += 1
            c -= 1
    for r in range(1,rows):
        c = cols-1
        while r<rows and c>=0 :
            result.append((r, c))
            r += 1
            c -= 1
    return result


def spiral_traversal(grid):
    """Iterates over a 2D list in spiral order and returning the coordinates (row, column)."""
    result = []
    rows = len(grid)
    cols = len(grid[0])

    #row/col definitions
    top = 0
    bottom = rows-1
    left = 0
    right = cols-1

    while top <= bottom and left <= right: #while in bounds
        #right
        for c in range(cols):
            r=top
            if((r,c)) not in result:
                result.append((top, c))
        top += 1

        #down
        for r in range(rows):
            c=right
            if((r,c)) not in result:
                result.append((r, right))
        right -= 1

        if top <= bottom: #if top hasn't crossed bottom
        #left
            for c in range(cols-1, - 1, -1):
                r=bottom
                if((r,c)) not in result:
                    result.append((bottom, c))
            bottom -= 1

        if left <= right: #if left hasn't crossed right
        #up
            for r in range(rows-1, - 1, -1):
                c=left
                if((r,c)) not in result:
                    result.append((r, left))
            left += 1
    return result
