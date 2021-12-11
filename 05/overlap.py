import re

with open('input.txt', 'r') as input:
    data = [[
        int(cord) for cord in re.split(r',|->', row)
        ] for row in input.read().split('\n')]

ocean_floar = dict()
overlap = 0


def make_entry(x, y) -> bool:
    if x not in ocean_floar:
        ocean_floar.update({x: {}})
    if y not in ocean_floar[x]:
        ocean_floar[x].update({y: 1})
        return False

    ocean_floar[x][y] += 1
    if ocean_floar[x][y] == 2:
        return True
    return False


for x1, y1, x2, y2 in data:
    if x1 < x2:
        rx = range(x1, x2+1)
    else:
        rx = range(x1, x2-1, -1)

    if y1 < y2:
        ry = range(y1, y2+1)
    else:
        ry = range(y1, y2-1, -1)

    if x1 == x2:
        x = x1
        for y in ry:
            if make_entry(x, y):
                 overlap += 1
        continue

    if y1 == y2:
        y = y1
        for x in rx:
            if make_entry(x, y):
                 overlap += 1
        continue

    iter_y = iter(ry)
    for x in rx:
        y = next(iter_y)
        if make_entry(x, y):
                overlap += 1

print(overlap)