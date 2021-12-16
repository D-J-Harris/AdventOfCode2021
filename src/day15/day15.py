from sys import maxsize
from queue import PriorityQueue

if __name__ == "__main__":

    class Cell:
        def __init__(self, x, y, val):
            self.x = x
            self.y = y
            self.val = val
            self.weight = maxsize
            self.visited = False
        
        def __lt__(self, other):
            return self.weight < other.weight

    grid = {}
    max_x, max_y = 0, 0
    with open('inputs/input-15.txt', 'r') as f:
        for x, line in enumerate(f.read().splitlines()):
            max_x = max(max_x, x)
            for y, val in enumerate(list(map(int, list(line)))):
                max_y = max(max_y, y)
                grid[(x, y)] = Cell(x, y, val)

    # amendments for part 2
    x_jump = max_x + 1
    y_jump = max_y + 1
    max_x = (5 * max_x) + 4
    max_y = (5 * max_y) + 4
    for (x, y), cell in grid.copy().items():
        val = cell.val
        for x_incr, x_val_incr in zip([x_jump, 2*x_jump, 3*x_jump, 4*x_jump], [1, 2, 3, 4]):
            grid[(x + x_incr, y)] = Cell(x + x_incr, y, ((val + x_val_incr - 1) % 9) + 1)
            for y_incr, y_val_incr in zip([y_jump, 2*y_jump, 3*y_jump, 4*y_jump], [1, 2, 3, 4]):
                grid[(x, y + y_incr)] = Cell(x, y + y_incr, ((val + y_val_incr - 1) % 9) + 1)
                grid[(x + x_incr, y + y_incr)] = Cell(x + x_incr, y + y_incr, ((val + x_val_incr + y_val_incr - 1) % 9) + 1)

    def neighbours(x, y):
        result = []
        for x, y in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
            if x > -1 and y > -1 and x <= max_x and y <= max_y:
                result.append(grid[(x, y)])
        return result

    
    queue = PriorityQueue()
    for cell in neighbours(0, 0):
        cell.weight = cell.val
        queue.put(cell)

    curr = queue.get()
    while curr.x != max_x or curr.y != max_y:
        if not curr.visited:
            nexts = [cell for cell in neighbours(curr.x, curr.y) if not cell.visited]
            for cell in nexts:
                if curr.weight + cell.val < cell.weight:
                    cell.weight = curr.weight + cell.val
                queue.put(cell)
            curr.visited = True
        curr = queue.get()

    print(f'answer to the puzzle is {curr.weight}')
