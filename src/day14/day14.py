from functools import lru_cache
from collections import Counter

if __name__ == "__main__":

    with open('inputs/input-14.txt', 'r') as f:
        rules = {}
        for i, line in enumerate(f.read().splitlines()):
            if i == 0:
                polymer = line
            elif i > 1:
                pattern, insert = line.split(' -> ')
                rules[pattern] = insert

    """
    Recursive calls on the pairs formed by inserting an element between each pair of elements
    At the bottom level, updates count of first element in the pair (not second, to avoid double-counting)
    This ends up counting the final polymer elements, minus the far rightmost element

    e.g. 
    NC -> NBC with 1 step
    splits into NB with 0 steps left -> update count of N by one
       and into BC with 0 steps left -> update count of B by one
    counting the final element is handled by the caller
    """
    @lru_cache(maxsize=None)
    def solve(string, steps):
        ans = Counter({})
        for i in range(len(string) - 1):
            substring = string[i: i + 2]
            if steps == 0:
                ans += Counter({string[0]: 1})
            else:
                ans += solve(substring[0] + rules[substring], steps - 1)
                ans += solve(rules[substring] + substring[1], steps - 1)
        return ans

    counts = lambda steps: solve(polymer, steps) + Counter({polymer[-1]: 1})
    diff = lambda c: c.most_common()[0][1] - c.most_common()[-1][1]
    print(f'answer to puzzle 1 is {diff(counts(10))}')
    print(f'answer to puzzle 2 is {diff(counts(40))}')
