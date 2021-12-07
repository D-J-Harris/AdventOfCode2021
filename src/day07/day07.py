
if __name__ == "__main__":

    with open('inputs/input-07.txt', 'r') as f:
        inp = list(map(int, f.readline().split(',')))

    def sumn(n):
        return (n * (n + 1)) // 2

    def solve(part_1):
        mn, mx = min(inp), max(inp)
        nums = [x - mn for x in inp] if part_1 else [sumn(x - mn) for x in inp]
        best_fuel = sum(nums)

        for i in range(mn + 1, mx + 1):
            nums = [abs(x - i) for x in inp] if part_1 else [sumn(abs(x - i)) for x in inp]
            sm = sum(nums)
            if sm < best_fuel:
                best_fuel = sm
        return best_fuel
    
    ans1 = solve(True)
    ans2 = solve(False)
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
