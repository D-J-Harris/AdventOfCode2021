from collections import defaultdict
from itertools import product

if __name__ == "__main__":

    # xs_range = list(range(20, 31))
    # ys_range = list(range(-10, -4))
    # specials = [6, 7]
    # trick_shot = 9

    xs_range = list(range(269, 293))
    ys_range = list(range(-68, -43))
    specials = [23]  # x velocities that stop in target area
    trick_shot = 67  # answer to part 1; max y velocity

    """ xs """
    # using n (n + 1) / 2, for only x = 23 we 'settle' inside of the xs
    # we also know we can make it in one step where x === xs for x in xs

    def get_x_vels(xs):
        lower = 1
        ans = defaultdict(list)  # (x_vel, steps_to_target)
        for upper in range(min(specials), xs[-1] + 1):
            while sum(range(lower, upper + 1)) not in xs and lower <= upper:
                lower += 1
            curr_lower = lower
            while sum(range(curr_lower, upper + 1)) in xs:
                steps = upper - curr_lower + 1
                ans[steps].append(upper)
                curr_lower += 1
        return ans

    """ ys """
    # we already know the highest y velocity as 67 from part 1 (no code needed)
    # this can go down to a minimum of -68, for one step

    def get_y_vels(ys):
        max_steps = (2 * trick_shot) + 2
        ans = defaultdict(list)  # (y_vel, steps_to_target)
        lower = min(ys)
        for steps in range(1, max_steps + 1):
            while sum([x for x in range(lower - (steps - 1), lower + 1)]) < ys[0] and lower <= trick_shot:
                lower += 1
            curr_lower = lower
            while sum([x for x in range(curr_lower - (steps - 1), curr_lower + 1)]) in ys:
                ans[steps].append(curr_lower)
                curr_lower += 1
        return ans







                
    x_vels = get_x_vels(xs_range)   
    y_vels = get_y_vels(ys_range)

    print(x_vels)
    print('\n')
    print(y_vels)

    ans = 0
    visited = set([])
    for steps, vals in y_vels.items():
        if steps in x_vels:
            for x_vel, y_vel in product(x_vels[steps], vals):
                ans += 1 if (x_vel, y_vel) not in visited else 0
                visited.add((x_vel, y_vel))
        for special in specials:
            if steps > special:
                for x_vel, y_vel in product(x_vels[special], vals):
                    ans += 1 if (x_vel, y_vel) not in visited else 0
                    visited.add((x_vel, y_vel))
        # ans += len(vals) * sum([steps > x for x in specials])

    print(f'answer to puzzle is {ans}')
