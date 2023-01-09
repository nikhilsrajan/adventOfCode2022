import typing


class Knot2:
    def __init__(self):
        self.head = (0, 0)
        self.tail = (0, 0)
        self.tail_trail = [self.tail]

    def move_tail(self):
        hx, hy = self.head
        tx, ty = self.tail

        while True:
            dx = hx - tx
            dy = hy - ty

            if abs(dx) <= 1 and abs(dy) <= 1:
                break

            if abs(dx) > 0:
                tx += dx // abs(dx)
            
            if abs(dy) > 0:
                ty += dy // abs(dy)
        
        self.tail = (tx, ty)
        self.tail_trail.append(self.tail)


    def move_one(self, direction):
        hx, hy = self.head

        if direction == 'U':
            hy += 1
        elif direction == 'D':
            hy -= 1
        elif direction == 'R':
            hx += 1
        elif direction == 'L':
            hx -= 1
        else:
            raise ValueError("direction must be from ['U', 'D', 'L', 'R']")
        
        self.head = (hx, hy)

        self.move_tail()


    def move(self, direction, steps):
        for _ in range(steps):
            self.move_one(direction=direction)


class KnotN:
    def __init__(self, N=2):
        if N < 2:
            raise ValueError('Must have at least 2 knots.')
        self.knots:typing.List[Knot2] = []
        for _ in range(N-1):
            self.knots.append(Knot2())
    
    def move_one(self, direction):
        p_tail = None
        for index in range(len(self.knots)):
            if index == 0:
                self.knots[index].move_one(direction=direction)
            else:
                self.knots[index].head = p_tail
                self.knots[index].move_tail()
            p_tail = self.knots[index].tail
    

    def move(self, direction, steps):
        for _ in range(steps):
            self.move_one(direction=direction)


def get_grid(list_of_pos:list, blank='.'):
    xs, ys = [], []
    for x, y in list_of_pos:
        xs.append(x)
        ys.append(y)
    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs)
    max_y = max(ys)
    x_extent = max_x - min_x
    y_extent = max_y - min_y
    grid = []
    for _ in range(y_extent+1):
        row = []
        for _ in range(x_extent+1):
            row.append(blank)
        grid.append(row)
    return grid, max_y, min_x


def print_trail(tail_trail:list, blank='.', fill='#'):
    tail_trail_set = set(tail_trail)
    grid, max_y, min_x = get_grid(list_of_pos=tail_trail_set, blank=blank)
    for x, y in tail_trail_set:
        grid[max_y - y][x - min_x] = fill
    return '\n'.join([''.join(row) for row in grid])


def print_knots(kN:KnotN, blank='.'):
    knots_pos = {'H': kN.knots[0].head}
    knot_names = ['H']
    for index, knot in enumerate(kN.knots, start=1):
        knots_pos[str(index)] = knot.tail
        knot_names.append(str(index))
    grid, max_y, min_x = get_grid(list_of_pos=list(knots_pos.values()), blank=blank)
    for knot_name in reversed(knot_names):
        x, y = knots_pos[knot_name]
        grid[max_y - y][x - min_x] = knot_name
    return '\n'.join([''.join(row) for row in grid])
