from statistics import multimode

if __name__ == "__main__":

    numbers = []
    with open('inputs/input-03.txt', 'r') as f:

        for b in f.read().splitlines():
            numbers.append(b)

    def get_gamma(inp):
        l = lambda x: sorted(multimode(x), reverse=True)[0]
        return ''.join(list(map(l, zip(*inp))))

    x = int(get_gamma(numbers), 2)
    n = len(numbers[0])
    ans1 = x * (2**n - 1 - x)


    def get_ox_or_co(inp, ox_requested):
        counter = 0
        while len(inp) > 1:
            inp = list(filter(lambda x: (x[counter] == get_gamma(inp)[counter]) == ox_requested, inp))
            counter += 1
        return int(inp[0], 2)

    ox = get_ox_or_co(numbers, True)
    co = get_ox_or_co(numbers, False)
    ans2 = ox * co

    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')

