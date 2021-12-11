with open('input.txt', 'r') as input:
    data = [list(row) for row in input.read().split('\n')]

print(data)

test = list()
slope, prev_slope = [0]*2, [0]*2

for i_row, row in enumerate(data):
    for i_v, v in enumerate(row):
        # check next row
        if i_row + 1 != len(data):
            slope[0] = 1 if v <= data[i_row+1][i_v] else -1
        else:
            slope[0] = 1

        # check next val
        if i_v + 1 != len(row):
            slope[1] = 1 if v <= row[i_v+1] else -1
        else:
            slope[1] = 1

        print(prev_slope, slope, v)
        prev_slope = slope