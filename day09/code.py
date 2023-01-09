from knot import KnotN


k10 = KnotN(N=10)
with open('input.txt', 'r') as h:
    for line in h.readlines():
        line.replace('\n', '')
        direction, steps = line.split(' ')
        steps = int(steps)
        k10.move(direction=direction, steps=steps)


print('task 1:', len(set(k10.knots[0].tail_trail)))
print('task 2:', len(set(k10.knots[-1].tail_trail)))
