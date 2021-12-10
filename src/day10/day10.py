from statistics import median
from collections import deque

if __name__ == "__main__":

    braces = {
        'starts': {
            '(': {
                "complement": ')',
                "value_auto": 1
            },
            '[': {
                "complement": ')',
                "value_auto": 2
            },
            '{': {
                "complement": '}',
                "value_auto": 3
            },
            '<': {
                "complement": '>',
                "value_auto": 4
            }
        },
        'ends': {
            ')': {
                "complement": '(',
                "value_syntax": 3,
            },
            ']': {
                "complement": '[',
                "value_syntax": 57,
            },
            '}': {
                "complement": '{',
                "value_syntax": 1197,
            },
            '>': {
                "complement": '<',
                "value_syntax": 25137,
            }
        }
    }

    ans1 = 0
    scores = []
    with open('inputs/input-10.txt', 'r') as f:
        for line in f.read().splitlines():
            corrupted = False
            stack = deque()
            for brace in line:
                if brace in braces['starts'].keys():
                    stack.append(brace)
                else:
                    if braces['ends'][brace]['complement'] != stack.pop():
                        ans1 += braces['ends'][brace]['value_syntax']
                        corrupted = True

            if not corrupted:
                score = 0
                while stack:
                    score = (5 * score) + braces['starts'][stack.pop()]['value_auto']
                scores.append(score)

    ans2 = median(sorted(scores))
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
