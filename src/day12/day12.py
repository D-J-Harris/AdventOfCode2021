from collections import deque

if __name__ == "__main__":

    class Cave:
        def __init__(self, name, is_small):
            self.name = name
            self.is_small = is_small
            self.neighbours = []

        def add_neighbour(self, cave):
            if cave not in self.neighbours:
                self.neighbours.append(cave)
                cave.neighbours.append(self)


    with open('inputs/input-12.txt', 'r') as f:
        caves = {}
        for line in f.read().splitlines():
            first, second = line.split('-')
            for c in [first, second]:
                if c not in caves:
                    cave = Cave(c, c.islower())
                    caves[c] = cave
            caves[first].add_neighbour(caves[second])

    def solve(is_part_two):
        paths = deque([[caves['start']]])
        ans = 0
        while paths:
            path = paths.popleft()
            latest = path[-1]
            if latest.name == 'end':
                ans += 1
            else:
                for n in latest.neighbours:
                    if not (n.name.islower() and n in path):
                        paths.append(path + [n])
                    elif n.name != 'start' and path[0] != 'double_added' and is_part_two:
                        paths.append(['double_added'] + path + [n])
        return ans
    
    ans1 = solve(False)
    ans2 = solve(True)
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
