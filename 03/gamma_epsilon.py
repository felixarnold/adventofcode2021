with open('input.txt', 'r') as input:
    data = input.read().split('\n')

gamma = 0
epsilon = 0

counts = [0,0,0,0,0,0,0,0,0,0,0,0]

for d in data:
    for i, c in enumerate(d):
        if int(c) > 0:
            counts[i] += 1

for count in counts:
    gamma = gamma << 1
    epsilon = epsilon << 1

    if count > 500:
        gamma = gamma | 1
    else:
        epsilon |= 1

print(epsilon * gamma)