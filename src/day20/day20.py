import numpy as np

if __name__ == "__main__":

    with open('inputs/input-20.txt', 'r') as f:
        inp = []
        for i, line in enumerate(f.read().splitlines()):
            if i < 1:
                algorithm = [0 if x == '.' else 1 for x in line]
            elif i > 1:
                inp.append([0 if x == '.' else 1 for x in line])

    def solve(steps, matrix):
        padding = 0
        matrix = np.array(matrix)
        for step_num in range(steps):
            matrix = np.pad(matrix, 2, mode='constant', constant_values=(padding:=(algorithm[int(f'{padding}'*9, 2)] if step_num != 0 else 0)))
            nxt = matrix[1:-1, 1:-1].copy()
            for i in range(len(matrix) - 2):
                for j in range(len(matrix[0]) - 2):
                    window = matrix[i: i+3, j: j+3]
                    nxt[i, j] = algorithm[int(''.join([str(x) for x in window.ravel()]), 2)]
            matrix = nxt
        return np.count_nonzero(matrix)

    print(f'answer to puzzle 1 is {solve(2, inp)}')
    print(f'answer to puzzle 2 is {solve(50, inp)}')
