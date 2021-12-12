import sys

# sys.setrecursionlimit(20000)
# print(sys.getrecursionlimit())

with open('input.txt', 'r') as input:
    data = [list(row) for row in input.read().split('\n')]

risk_level = 0
low_point_pos = []


def basin_size(i_row, i_v, len_row, dir=0) -> int:
    if data[i_row][i_v] >= '9':
        print(9)
        return 0

    res = 1
    if i_row > 0 and dir != 3:
        res += basin_size(i_row-1, i_v, len_row, 1)

    if i_v < len_row - 1 and dir != 4:
        res += basin_size(i_row, i_v+1, len_row, 2)

    if i_row < len(data) - 1 and dir != 1:
        res += basin_size(i_row+1, i_v, len_row, 3)

    if i_v > 0 and dir != 2:
        res += basin_size(i_row, i_v-1, len_row, 4)

    return res


slope_y = [[1]*len(data[1]), [1]*len(data[1])]
for i_row, row in enumerate(data):
    slope_x = [1]*2
    for i_v, v in enumerate(row):
        # check next row
        if i_row < len(data) - 1:
            slope_y[1][i_v] = int(v) - int(data[i_row+1][i_v])
        else:
            slope_y[1][i_v] = -1

        # check next val
        if i_v < len(row) - 1:
            slope_x[1] = int(v) - int(row[i_v+1])
        else:
            slope_x[1] = -1

        if slope_x[0] > 0 and slope_x[1] < 0:
            if slope_y[0][i_v] > 0 and slope_y[1][i_v] < 0:
                risk_level += 1 + int(v)
                print(basin_size(i_row, i_v, len(row)))

        slope_x.insert(0, slope_x.pop(1))
    slope_y.insert(0, slope_y.pop(1))

print(risk_level)
