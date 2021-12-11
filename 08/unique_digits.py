with open('input.txt','r') as input:
    data = [[[
        v for v in groups.split()
                ] for groups in line.split('|')
            ] for line in input.read().split('\n')
        ]

count = 0

for groups in data:
    for num in groups[1]:
        if len(num) in [2, 3, 4, 7]:
            count += 1

print(count)