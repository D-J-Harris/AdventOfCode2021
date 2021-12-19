from scipy.signal import correlate2d
from collections import defaultdict
import numpy as np
import re
import sys

if __name__ == "__main__":

    with open('inputs/input-19.txt', 'r') as f:
        coords = defaultdict(list)
        mins_x, mins_y = {}, {}
        ranges_x, ranges_y = {}, {}
        scans = {}
        for scanner in f.read().split('\n\n'):
            max_x, max_y = 0, 0
            min_x, min_y = 0, 0
            for line in scanner.split('\n'):
                if (matched := re.search(r'scanner (\d+)', line)):
                    scanner_num = int(matched.group(1))
                else:
                    x, y = map(int, line.split(','))
                    max_x, max_y = max(max_x, x), max(max_y, y)
                    min_x, min_y = min(min_x, x), min(min_y, y)
                    coords[scanner_num].append(np.array([x, y]))
            mins_x[scanner_num], mins_y[scanner_num] = min_x, min_y
            ranges_x[scanner_num], ranges_y[scanner_num] = max_x - min_x + 1, max_y - min_y + 1
            coords[scanner_num] = [coord - [mins_x[scanner_num], mins_y[scanner_num]] for coord in coords[scanner_num]]
            scan = np.zeros((ranges_x[scanner_num], ranges_y[scanner_num]))
            for x, y in coords[scanner_num]:
                scan[x, y] = 1
            scans[scanner_num] = scan

    print(scans[0])
    print('\n')
    print(scans[1])
    print('\n')

    print(c:= correlate2d(scans[0], scans[1], 'full'))
    print(correlate:= np.argwhere(c >= 3)[0])
    print('\n')

    # scanner 1 coords relative to scanner 0
    scanner_num = 1

    for coordinates in coords[scanner_num]:
        print(coordinates)
        print([coordinates[0] - (ranges_x[scanner_num] - 1) + correlate[0],coordinates[1] - (ranges_y[scanner_num] - 1) + correlate[1]])
        print('\n')

