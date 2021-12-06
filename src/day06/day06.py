import functools

if __name__ == "__main__":

    with open('inputs/input-06.txt', 'r') as f:
        inp = list(map(int, f.readline().split(',')))

    @functools.lru_cache(maxsize=None)
    def fish_for_days_left(days, timer):
        return 1 + fish_for_days_left(days - timer - 1, 6) + fish_for_days_left(days - timer - 1, 8) if days > timer else 0

    ans1 = len(inp) + sum([fish_for_days_left(80, num) for num in inp])
    ans2 = len(inp) + sum([fish_for_days_left(256, num) for num in inp])
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
