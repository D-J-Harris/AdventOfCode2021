
if __name__ == "__main__":

    h = 0
    d1, d2 = 0, 0
    a = 0
    with open('inputs/input-02.txt', 'r') as f:
        for line in f.readlines():
            cmd, val = line.split(' ')
            val = int(val)
            match cmd:
                case 'forward':
                    h += val
                    d2 += a * val
                case 'down':
                    d1 += val
                    a += val
                case 'up':
                    d1 -= val
                    a -= val
                case _:
                    raise "hell"

    ans1 = h * d1
    ans2 = h * d2
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
