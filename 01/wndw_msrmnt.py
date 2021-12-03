with open('input.txt', 'r') as input:
    data = input.read().split('\n')

count = 0
prev_win = None
vals = [None, None, None]

for d in data:
    vals.insert(0, int(d))
    del vals[-1]

    if None in vals:
        continue

    win = sum(vals)

    if prev_win is not None and win > prev_win:
        count += 1

    prev_win = win

print(count)