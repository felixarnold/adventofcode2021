with open('input.txt', 'r') as input:
    data = input.read().split('\n')

hor = 0
dep = 0

for d in data:
    inst, val = d.split()

    if 'forward' == inst:
        hor += int(val)

    if 'down' == inst:
        dep += int(val)

    if 'up' == inst:
        dep -= int(val)

print(hor * dep)
