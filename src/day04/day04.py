from collections import defaultdict, deque

if __name__ == "__main__":
    call_results = defaultdict(list)
    board_states = defaultdict(list)

    def key(board_num, code, dir_num):
        return ''.join([str(board_num), code, str(dir_num)])

    num_boards = 0
    with open('inputs/input-04.txt', 'r') as f:
        calls = deque(f.readline().split(','))
        f.readline()
        for board_num, board in enumerate(f.read().split('\n\n')):
            num_boards += 1
            for row_num, row in enumerate(board.split('\n')):
                for col_num, val in enumerate(row.split()):
                    board_states[key(board_num, 'r', row_num)].append(val)
                    board_states[key(board_num, 'c', col_num)].append(val)
                    call_results[val].append([board_num, row_num, col_num])

    def board_score(b, call):
        ans = 0
        for board_key in board_states.keys():
            board_num = board_key.split('r')[0].split('c')[0]
            if board_num == str(b):
                ans += sum(map(int, board_states[board_key]))
        return int(ans / 2) * int(call)

    winning_boards = defaultdict(str)
    bingo = False
    while not len(winning_boards) == num_boards:
        calling_num = calls.popleft()
        for loc in call_results[calling_num]:
            board_num, row_num, col_num = loc
            if board_num in winning_boards:
                continue
            r_key, c_key = key(board_num, 'r', row_num), key(board_num, 'c', col_num)
            board_states[r_key].remove(calling_num)
            board_states[c_key].remove(calling_num)
            if not board_states[r_key] or not board_states[c_key]:
                winning_board = board_num
                winning_boards[winning_board] = calling_num
                if not bingo:
                    ans1 = board_score(winning_board, calling_num)
                    bingo = True

    ans2 = board_score(winning_board, calling_num)
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
