from collections import defaultdict
from itertools import product

if __name__ == "__main__":

    xs_range = list(range(269, 293))
    ys_range = list(range(-68, -43))
    max_yvel = 67  # answer to part 1; max y velocity

    # x velocities that stop in target area
    settled_xvels, n = [], 1
    while n * (n + 1) / 2 < xs_range[0]: n += 1
    while n * (n + 1) / 2 <= xs_range[-1]: settled_xvels.append(n); n += 1

    """ xs """
    # using n (n + 1) / 2, settled_xvels are x velocities that 'settle' inside of the xs range
    # we also know we can make it in one step with an x velocity of max(xs)
    # -> sum the window 1..23, and shift the lower then upper bounds to catch all x velocities
    # that will land in the target xs range in the given number of steps

    def get_x_vels(xs):
        lower = 1
        ans = defaultdict(list)  # (x_vel, steps_to_target)
        for upper in range(min(settled_xvels), xs[-1] + 1):
            for next_lower in range(lower, upper + 1):
                if sum(range(next_lower, upper + 1)) in xs:
                    lower = next_lower
                    curr_lower = lower
                    while sum(range(curr_lower, upper + 1)) in xs:
                        steps = upper - curr_lower + 1
                        ans[steps].append(upper)
                        curr_lower += 1
                    break
        return ans

    """ ys """
    # we already know the highest y velocity as 67 from part 1 (no code needed)
    # this can go down to a minimum of -68, for a step trajectory straight into target ys
    # using the number of steps taken for the max_yvel shot to land as a max, we get all y velocities
    # that will land in the target ys range in the given number of steps

    def get_y_vels(ys):
        max_steps = (2 * max_yvel) + 2
        ans = defaultdict(list)  # (y_vel, steps_to_target)
        lower = min(ys)
        for steps in range(1, max_steps + 1):
            while sum([x for x in range(lower - (steps - 1), lower + 1)]) < ys[0] and lower <= max_yvel:
                lower += 1
            curr_lower = lower
            while sum([x for x in range(curr_lower - (steps - 1), curr_lower + 1)]) in ys:
                ans[steps].append(curr_lower)
                curr_lower += 1
        return ans
           
    x_vels = get_x_vels(xs_range)   
    y_vels = get_y_vels(ys_range)

    ans = 0
    visited = set([])
    for steps, vals in y_vels.items():
        if steps in x_vels:
            for x_vel, y_vel in product(x_vels[steps], vals):
                ans += 1 if (x_vel, y_vel) not in visited else 0
                visited.add((x_vel, y_vel))
        for settled_xvel in settled_xvels:
            if steps > settled_xvel:
                for x_vel, y_vel in product(x_vels[settled_xvel], vals):
                    ans += 1 if (x_vel, y_vel) not in visited else 0
                    visited.add((x_vel, y_vel))
    print(f'answer to puzzle is {ans}')
