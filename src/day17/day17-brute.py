# regrettably, this runs faster than the other analytical solution

import re 
if __name__ == "__main__":

    with open('inputs/input-17.txt', 'r') as f:
        pattern = r'[xy]=(-?\d+)..(-?\d+)'
        res = re.findall(pattern, f.readline().strip())
        xs_range = list(range(int(res[0][0]), int(res[0][1]) + 1))
        ys_range = list(range(int(res[1][0]), int(res[1][1]) + 1))
    max_yv = - (ys_range[0] + 1)  # answer to part 1; max y velocity

    def launch(xv, yv):
        if xv == 0 and yv == 0:
            return 0
        x = 0
        y = 0

        while not x > xs_range[-1] and not y < ys_range[0]:
            x += xv if xv else 0
            y += yv
            xv -= 1 if xv else 0
            yv -= 1
            if xs_range[0] <= x <= xs_range[-1] and ys_range[0] <= y <= ys_range[-1]:
                return 1
        return 0

    ans2 = 0
    for x_vel in range(xs_range[-1] + 1):
        for y_vel in range(ys_range[0], max_yv + 1):
            ans2 += launch(x_vel, y_vel)

    ans1 = int(max_yv * (max_yv + 1) / 2)
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
