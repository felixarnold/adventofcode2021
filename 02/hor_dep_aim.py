with open('input.txt', 'r') as input:
    data = input.read().split('\n')

hor = 0
dep = 0
aim = 0

for d in data:
    inst, val = d.split()

    if 'forward' == inst:
        hor += int(val)
        dep += int(val) * aim

    if 'down' == inst:
        aim += int(val)

    if 'up' == inst:
        aim -= int(val)

print(hor * dep)
