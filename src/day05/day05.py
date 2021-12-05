import numpy as np
from itertools import repeat

if __name__ == "__main__":

    max_x, max_y = 0, 0
    pairs = []
    with open('inputs/input-05.txt', 'r') as f:
        for line in f.read().splitlines():
            start, end = line.split(' -> ')
            x_start, y_start = map(int, start.split(','))
            x_end, y_end = map(int, end.split(','))
            max_x = max(max_x, x_start, x_end)
            max_y = max(max_y, y_start, y_end)
            pairs.append([(x_start, y_start), (x_end, y_end)])

    def solve(grid, is_part_2):
        for pair in pairs:
            (x_start, y_start), (x_end, y_end) = pair[0], pair[1]
            x_rev = 2 * (x_start < x_end) - 1
            y_rev = 2 * (y_start < y_end) - 1
            x_range = range(x_start, x_end + x_rev, x_rev)
            y_range = range(y_start, y_end + y_rev, y_rev)
            if x_start == x_end:
                for x, y in zip(repeat(x_start), y_range):
                    grid[x, y] += 1
            elif y_start == y_end:
                for x, y in zip(x_range, repeat(y_start)):
                    grid[x, y] += 1
            else:
                if is_part_2: 
                    for x, y in zip(x_range, y_range):
                        grid[x, y] += 1
        return np.count_nonzero(grid > 1)

    grid = np.zeros((max_x+1, max_y+1))
    ans1 = solve(grid, False)
    grid = np.zeros((max_x+1, max_y+1))
    ans2 = solve(grid, True)

    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')