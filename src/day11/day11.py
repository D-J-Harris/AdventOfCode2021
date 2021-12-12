import numpy as np
from collections import deque
from itertools import product

if __name__ == "__main__":

    class Grid:
        def __init__(self, grid):
            self.grid = grid
            self.height = len(self.grid)
            self.width = len(self.grid[0])
            self.flashes = 0
            self.num_steps = 0

        def neighbours(self, x, y):
            lx, ly = self.height, self.width
            result = []
            for xd, yd in product([-1, 0, 1], [-1, 0, 1]):
                x_new, y_new = x + xd, y + yd
                if not (xd == 0 and yd == 0) and x_new > -1 and y_new > -1 and x_new < lx and y_new < ly:
                    result.append((x_new, y_new))
            return result

        def step(self):
            self.grid += 1
            stack = deque(np.argwhere(self.grid == 10))
            to_reset = []
            while stack:
                x, y = stack.pop()
                to_reset.append([x, y])
                for xn, yn in self.neighbours(x, y):
                    self.grid[xn][yn] += 1
                    if self.grid[xn][yn] == 10:
                        stack.append([xn, yn])
            for x, y in to_reset:
                self.flashes += 1
                self.grid[x][y] = 0
            self.num_steps += 1

            # returns step number if step was 'synchronised'
            return self.num_steps if len(to_reset) == self.width * self.height else None

    rows = []
    with open('inputs/input-11.txt', 'r') as f:
        for line in f.read().splitlines():
            rows.append(list(map(int, list(line))))
        grid = Grid(np.array(rows))

    num_steps = 100
    sync_steps = []
    for _ in range(num_steps):
        if step := grid.step():
            sync_steps.append(step)
    ans1 = grid.flashes

    while not sync_steps:
        if step := grid.step():
            sync_steps.append(step)
    
    ans2 = sync_steps[0]
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
