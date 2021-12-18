from ast import literal_eval
from math import floor, ceil
import re

if __name__ == "__main__":

    class SnailFish:
        def __init__(self, inp):
            self.pair = literal_eval(inp) if isinstance(inp, str) else inp
            self.left = self.pair[0]
            self.right = self.pair[1]
            self.magnitude = SnailFish.calculate_magnitude(self.left, self.right)

        @staticmethod
        def calculate_magnitude(left, right):
            if isinstance(left, list):
                left = SnailFish.calculate_magnitude(left[0], left[1])
            if isinstance(right, list):
                right = SnailFish.calculate_magnitude(right[0], right[1])
            return (3 * left) + (2 * right)

        @classmethod
        def add_together(cls, left, right):
            assert(isinstance(left, SnailFish) and isinstance(right, SnailFish))
            snailfish = SnailFish([left.pair, right.pair])
            print(snailfish.pair)
            reduced = False
            while not reduced:
                if cls.__explode(snailfish):
                    print(snailfish.pair)
                    continue
                reduced = cls.__split(snailfish)
            print('haha ', snailfish.pair)

            
        
        def __explode(snailfish):
            string = str(snailfish.pair)
            str_iterator = enumerate(string)

            open_brackets, open_loc, close_loc = 0, None, None
            left_element, right_element = '', ''
            while (nxt := next(str_iterator)) is not None:
                open_brackets += 1 if nxt[1] == '[' else 0
                open_brackets -= 1 if nxt[1] == ']' else 0
                if open_brackets == 5:
                    open_loc = nxt[0]
                    while (nxt := next(str_iterator))[1] != ',':
                        left_element += nxt[1]
                    while (nxt := next(str_iterator))[1] != ']':
                        right_element += nxt[1]
                    close_loc = nxt[0]
                    left_element, right_element = int(left_element), int(right_element)
                    break

            if matched := re.search(r'^\D*(\d+)', string[close_loc:]):
                string = string[:close_loc] + re.sub(r'^(\D*)\d+', fr'\1 {right_element + int(matched.group(1))}', string[close_loc:])
            string = string[:open_loc] + '0' + string[close_loc + 1:]
            if matched := re.search(r'(\d+)\D*$', string[:open_loc]):
                string = re.sub(r'\d+(\D*)$', fr'{left_element + int(matched.group(1))}\1', string[:open_loc]) + string[open_loc:]
            snailfish.pair = string
            return True if open_brackets else False
        
        def __split(snailfish):
            string = str(snailfish.pair)
            if matched := re.search(r'\d{2,}(.*)', string):
                num = int(matched.group(1))
                string = re.sub(r'(\d{2,}).*', fr'{[floor(num / 2), ceil(num / 2)]}\1')

            snailfish.pair = string
            return True if matched else False



                




    with open('inputs/input-18.txt', 'r') as f:
        snailfish = []
        for line in f.read().splitlines():
            snailfish.append(SnailFish(line))

    one_snail = SnailFish(r'[[[[4,3],4],4],[7,[[8,4],9]]]')
    two_snail = SnailFish(r'[1,1]')
    # one_snail = SnailFish(r'[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
    # two_snail = SnailFish(r'[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
    res = SnailFish.add_together(one_snail, two_snail)
    print('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')

    # string = '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'
    # open = 16
    # close = 20
    # print(string)
    # matched_num = re.search(r'^\D*(\d+)', string[close:]).group(1)
    # print(matched_num)
    # string = string[:close] + re.sub(r'^(\D*)\d+', fr'\1 {12 + int(matched_num)}', string[close:])
    # print(string)
    # string = string[:open] + '0' + string[close + 1:]
    # print(string)
    # matched_num = re.search(r'(\d+)\D*$', string[:open]).group(1)
    # print(matched_num)
    # string = re.sub(r'\d+(\D*)$', fr'{12 + int(matched_num)}\1', string[:open]) + string[open:]
    # print(string)

    ans1 = 0
    print(f'answer to puzzle 1 is {ans1}')