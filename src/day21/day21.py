from functools import cache

if __name__ == "__main__":

    with open('inputs/input-21.txt', 'r') as f:
        players = [[], []]  # [pos, score] per player
        for player_num, line in enumerate(f.read().splitlines()):
            start_pos = int(line.split(' ')[-1])
            players[player_num] = [start_pos, 0]

    def part_1(pos_one, pos_two, score_one, score_two):
        player_num, die = 0, -1
        while score_one < 1000 and score_two < 1000:
            if player_num:
                pos_two = ((pos_two - 1) + 3 * (die:= die + 3)) % 10 + 1
                score_two += pos_two
            else:
                pos_one = ((pos_one - 1) + 3 * (die:= die + 3)) % 10 + 1
                score_one += pos_one
            player_num = 1 - player_num
        return min(score_one, score_two) * (die + 1)

    @cache
    def part_2(pos_player, pos_other, score_player, score_other):
        if score_player >= 21:
            return 1, 0
        if score_other >= 21:
            return 0, 1

        wins_player_tot, wins_other_tot = 0, 0

        # (sum, count) for each of 27 universes three die rolls can lead to
        universes = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]
        for sum, count in universes:
            pos_new = (pos_player + sum - 1) % 10 + 1
            score_new = score_player + pos_new

            wins_other, wins_player = part_2(pos_other, pos_new, score_other, score_new)
            wins_player_tot += wins_player * count
            wins_other_tot += wins_other * count

        return wins_player_tot, wins_other_tot

    ans1 = part_1(players[0][0], players[1][0], players[0][1], players[1][1])
    ans2 = max(part_2(players[0][0], players[1][0], players[0][1], players[1][1]))
    print(f'answer to puzzle 1 is {ans1}')
    print(f'answer to puzzle 2 is {ans2}')
