import numpy as np


def is_visible(r:int, c:int, tree_grid:np.ndarray):
    n_rows, n_cols = tree_grid.shape

    if r == 0 or c == 0 or r == n_rows-1 or c == n_cols-1:
        return True

    tree_h = tree_grid[r,c]

    if np.max(tree_grid[:r,c]) < tree_h:
        return True
    
    if np.max(tree_grid[r+1:,c]) < tree_h:
        return True
    
    if np.max(tree_grid[r,:c]) < tree_h:
        return True

    if np.max(tree_grid[r,c+1:]) < tree_h:
        return True
    
    return False


def get_scenic_score(r:int, c:int, tree_grid:np.ndarray):
    n_rows, n_cols = tree_grid.shape

    if r == 0 or c == 0 or r == n_rows-1 or c == n_cols-1:
        return 0

    tree_h = tree_grid[r,c]
    
    top = 0
    for r_i in range(r-1, -1, -1):
        top += 1
        if tree_grid[r_i, c] >= tree_h:
            break
        

    bottom = 0
    for r_i in range(r+1, n_rows):
        bottom += 1
        if tree_grid[r_i, c] >= tree_h:
            break
    
    right = 0
    for c_i in range(c-1, -1, -1):
        right += 1
        if tree_grid[r, c_i] >= tree_h:
            break
    
    left = 0
    for c_i in range(c+1, n_cols):
        left += 1
        if tree_grid[r, c_i] >= tree_h:
            break
    
    return top * bottom * right * left


def apply(tree_grid:np.ndarray, func):
    res_grid = np.zeros(tree_grid.shape)
    n_rows, n_cols = tree_grid.shape
    for r in range(n_rows):
        for c in range(n_cols):
            res_grid[r,c] = func(
                r=r, c=c, tree_grid=tree_grid,
            )
    return res_grid



tree_grid = []
with open('input.txt', 'r') as h:
    for line in h.readlines():
        line = line.replace('\n', '')
        tree_row = []
        for tree_str in line:
            tree_row.append(int(tree_str))
        tree_grid.append(tree_row)
tree_grid = np.array(tree_grid)


visibility_grid = apply(tree_grid=tree_grid, func=is_visible).astype(int)
print('task 1:', visibility_grid.sum())

scenic_score_grid = apply(tree_grid=tree_grid, func=get_scenic_score).astype(int)
print('task 2:', scenic_score_grid.max())
