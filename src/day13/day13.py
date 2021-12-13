import numpy as np
np.set_printoptions(linewidth=200)

if __name__ == "__main__":

    with open('inputs/input-13.txt', 'r') as f:
        instructions = []
        points = []
        max_x, max_y = 0, 0
        for line in f.read().splitlines():
            if not line:
                pass
            elif line[:4].startswith('fold'):
                _, _, fold = line.split()
                dir, pos = fold.split('=')
                instructions.append((dir, int(pos)))
            else:
                y, x = map(int, line.split(','))
                max_x, max_y = max(max_x, x), max(max_y, y)
                points.append((x, y))

    grid = np.zeros((max_x + 1, max_y + 1))
    for x, y in points:
        grid[x, y] = 1

    def fold(matrix, dir, pos):
        block = matrix[:, :pos] if 'x' in dir else matrix[pos + 1:, :]
        block = np.fliplr(block) if 'x' in dir else np.flipud(block)
        lx, ly = len(block), len(block[0])
        if 'x' in dir:
            matrix[:, pos + 1:pos + ly + 1] += block
            return matrix[:, pos + 1:]
        else:
            matrix[pos - lx:pos, :] += block
            return matrix[:pos, :]

    for i, (dir, pos) in enumerate(instructions):
        grid = fold(grid, dir, pos)
        if i == 0:
            print(f'answer to puzzle 1 is {np.count_nonzero(grid)}')

    # fead output for answer to part 2
    print(np.fliplr(np.where(grid > 0, '#', '.')))
