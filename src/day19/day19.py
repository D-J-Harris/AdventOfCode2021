from scipy.signal import correlate2d
from collections import defaultdict
from numpy import rot90
import numpy as np
import re

if __name__ == "__main__":

    with open('inputs/input-19.txt', 'r') as f:
        coords = defaultdict(list)
        mins_x, mins_y, mins_z = {}, {}, {}
        ranges_x, ranges_y, ranges_z = {}, {}, {}
        scans = {}
        for scanner in f.read().split('\n\n'):
            max_x, max_y, max_z = 0, 0, 0
            min_x, min_y, min_z = 0, 0, 0
            for line in scanner.split('\n'):
                if (matched := re.search(r'scanner (\d+)', line)):
                    scanner_num = int(matched.group(1))
                else:
                    x, y, z = map(int, line.split(','))
                    max_x, max_y, max_z = max(max_x, x), max(max_y, y), max(max_z, z)
                    min_x, min_y, min_z = min(min_x, x), min(min_y, y), min(min_z, z)
                    coords[scanner_num].append(np.array([x, y, z]))
            mins_x[scanner_num], mins_y[scanner_num], mins_z[scanner_num] = min_x, min_y, min_z
            ranges_x[scanner_num], ranges_y[scanner_num], ranges_z[scanner_num] = max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1
            coords[scanner_num] = [coord - [mins_x[scanner_num], mins_y[scanner_num], mins_z[scanner_num]] for coord in coords[scanner_num]]
            scan = np.zeros((ranges_x[scanner_num], ranges_y[scanner_num], ranges_z[scanner_num]))
            for x, y, z in coords[scanner_num]:
                scan[x, y, z] = 1
            scans[scanner_num] = scan
    

    def rotations24(polycube):
        def rotations4(polycube, axes):
            for i in range(4):
                yield rot90(polycube, i, axes)
        yield from rotations4(polycube, (1,2))
        yield from rotations4(rot90(polycube, 2, axes=(0,2)), (1,2))
        yield from rotations4(rot90(polycube, axes=(0,2)), (0,1))
        yield from rotations4(rot90(polycube, -1, axes=(0,2)), (0,1))
        yield from rotations4(rot90(polycube, axes=(0,1)), (0,2))
        yield from rotations4(rot90(polycube, -1, axes=(0,1)), (0,2))

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

