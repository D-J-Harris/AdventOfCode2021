import numpy as np
from collections import deque

if __name__ == "__main__":

    grid = []
    with open('inputs/input-09.txt', 'r') as f:
        for line in f.read().splitlines():
            grid.append(list(map(int, list(line))))
        grid = np.array(grid)


    def neighbours(matrix, x, y):
        lx, ly = len(matrix), len(matrix[0])
        result = []
        for x, y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if x > -1 and y > -1 and x < lx and y < ly:
                result.append((x, y))
        return result


    ans1 = 0
    for row_num, row in enumerate(grid):
        for col_num, val in enumerate(row):
            if all([val < grid[x][y] for x, y in neighbours(grid, row_num, col_num)]):
                ans1 += 1 + val

    basins = []
    for row_num, row in enumerate(grid):
        for col_num, val in enumerate(row):
            if val not in [-1, 9]:
                basin_size = 1
                grid[row_num][col_num] = -1
                d = deque(neighbours(grid, row_num, col_num))
                while len(d) > 0:
                    candidate_x, candidate_y = d.popleft()
                    val = grid[candidate_x][candidate_y]
                    if val not in [-1, 9]:
                        basin_size += 1
                        grid[candidate_x][candidate_y] = -1
                        [d.append((x, y)) for x, y in neighbours(grid, candidate_x, candidate_y)]
                basins.append(basin_size)

    basins = sorted(basins)
    ans2 = basins[-1] * basins[-2] * basins[-3]
 
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
