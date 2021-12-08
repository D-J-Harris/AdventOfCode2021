
if __name__ == "__main__":

    with open('inputs/input-08.txt', 'r') as f:
        pairs = []
        for line in f.readlines():
            inp, out = line.split(' | ')
            inp, out = inp.split(), out.split()
            pairs.append((inp, out))

    def input_to_code(lst):
        code = {}
        for num in lst:
            num = ''.join(sorted(num))
            match len(num):
                case 2:
                    code['1'] = num
                case 3:
                    code['7'] = num
                case 4:
                    code['4'] = num
                case 7:
                    code['8'] = num
                case _: pass
        for num in lst:
            num = ''.join(sorted(num))
            match len(num):
                case 5:
                    if all([x in num for x in code['7']]):
                        code['3'] = num
                    elif sum([x in num for x in code['4']]) == 3:
                        code['5'] = num
                    else:
                        code['2'] = num
                case 6:
                    if all([x in num for x in code['4']]):
                        code['9'] = num
                    elif all([x in num for x in code['7']]):
                        code['0'] = num
                    else:
                        code['6'] = num
                case _: pass
        return code

    ans1 = 0
    ans2 = 0
    for inp, out in pairs:
        ans1 += len(list(filter(lambda x: len(x) in [2, 3, 4, 7], out)))
        code = {v: k for k, v in input_to_code(inp).items()}
        ans2 += int(''.join([code[''.join(sorted(x))] for x in out]))

    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
