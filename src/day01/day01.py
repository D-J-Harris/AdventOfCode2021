
if __name__ == "__main__":

    ans1 = 0
    ans2 = 0
    with open('inputs/input-01.txt', 'r') as f:
        inp = []
        for num in f.read().splitlines():
            inp.append(int(num))

    for i, num in enumerate(inp[1:]):
        if num > inp[i]:
            ans1 += 1

        if i > 1 and num > inp[i-2]:
            ans2 += 1

    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')