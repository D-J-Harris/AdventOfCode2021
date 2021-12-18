from ast import literal_eval
from math import floor, ceil
import re

if __name__ == "__main__":

    class SnailFish:
        def __init__(self, inp):
            self._pair = literal_eval(inp) if isinstance(inp, str) else inp
            self.left = self._pair[0]
            self.right = self._pair[1]

        def set_pair(self, inp):
            self._pair = literal_eval(inp) if isinstance(inp, str) else inp
            self.left = self._pair[0]
            self.right = self._pair[1]

        def get_pair(self):
            return self._pair

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
            snailfish = SnailFish([left.get_pair(), right.get_pair()])
            reduced = False
            while not reduced:
                if cls.__explode(snailfish):
                    continue
                reduced = not cls.__split(snailfish)
            return snailfish


        def __explode(snailfish):
            string = str(snailfish.get_pair())

            open_brackets, open_loc, comma_found, close_loc = 0, None, False, None
            left_element, right_element = '', ''
            for idx, char in enumerate(string):
                if open_brackets < 5:
                    open_brackets += 1 if char == '[' else 0
                    open_brackets -= 1 if char == ']' else 0
                    if open_brackets == 5:
                        open_loc = idx
                else:
                    if not comma_found:
                        if char == ',':
                            comma_found = True
                        else:
                            left_element += char
                    elif not close_loc:
                        if char == ']':
                            close_loc = idx
                            left_element, right_element = int(left_element), int(right_element)
                            break
                        else:
                            right_element += char

            if open_brackets == 5:
                if matched := re.search(r'^\D*(\d+)', string[close_loc:]):
                    string = string[:close_loc] + re.sub(r'^(\D*)\d+', fr'\1 {right_element + int(matched.group(1))}', string[close_loc:])
                string = string[:open_loc] + '0' + string[close_loc + 1:]
                if matched := re.search(r'(\d+)\D*$', string[:open_loc]):
                    string = re.sub(r'\d+(\D*)$', fr'{left_element + int(matched.group(1))}\1', string[:open_loc]) + string[open_loc:]
                snailfish.set_pair(string.replace(' ', ''))
                return True
            else:
                return False        
        

        def __split(snailfish):
            string = str(snailfish.get_pair())
            if matched := re.search(r'(\d{2,}).*', string):
                num = int(matched.group(1))
                string = re.sub(r'\d{2,}(.*)', fr'{[floor(num / 2), ceil(num / 2)]}\1', string)
                snailfish.set_pair(string.replace(' ', ''))
                return True
            else:
                return False

    with open('inputs/input-18.txt', 'r') as f:
        snailfish = []
        for line in f.read().splitlines():
            snailfish.append(SnailFish(line))

    res = snailfish[0]
    for sn in snailfish[1:]:
        res = res.add_together(res, sn)
    ans1 = SnailFish.calculate_magnitude(res.left, res.right)
    print(f'answer to puzzle 1 is {ans1}')

    ans2 = 0
    for idx, sn1 in enumerate(snailfish):
        for sn2 in snailfish[idx + 1:]:
            res = SnailFish.add_together(sn1, sn2)
            mag = SnailFish.calculate_magnitude(res.left, res.right)
            ans2 = max(ans2, mag)
            res = SnailFish.add_together(sn2, sn1)
            mag = SnailFish.calculate_magnitude(res.left, res.right)
            ans2 = max(ans2, mag)
    print(f'answer to puzzle 2 is {ans2}')
