from collections import defaultdict, deque

if __name__ == "__main__":
    call_results = defaultdict(list)
    board_states = defaultdict(list)

    def key(board_num, code, dir_num):
        return ''.join([str(board_num), code, str(dir_num)])


    with open('inputs/input-04.txt', 'r') as f:
        calls = deque(f.readline().split(','))
        f.readline()
        for board_num, board in enumerate(f.read().split('\n\n')):
            for row_num, row in enumerate(board.split('\n')):
                for col_num, val in enumerate(row.split()):
                    board_states[key(board_num, 'r', row_num)].append(val)
                    board_states[key(board_num, 'c', col_num)].append(val)
                    call_results[val].append([board_num, row_num, col_num])

    bingo = False
    
    while not bingo:
        calling_num = calls.popleft()
        for loc in call_results[calling_num]:
            board_num, row_num, col_num = loc
            r_key, c_key = key(board_num, 'r', row_num), key(board_num, 'c', col_num)
            board_states[r_key].remove(calling_num)
            board_states[c_key].remove(calling_num)
            if not board_states[r_key] or not board_states[c_key]:
                bingo = True
                winning_board = board_num

    ans1 = 0
    for board_key in board_states.keys():
        board_num = board_key.split('r')[0].split('c')[0]
        if board_num == str(winning_board):
            ans1 += sum(map(int, board_states[board_key]))
    ans1 = int((ans1 / 2 )) * int(calling_num)

    print(f'answer to puzzle 1 is {ans1}')
