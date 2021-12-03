with open('input.txt', 'r') as input:
    data = input.read().split('\n')

count = 0
prev = None
for d in data:
    if prev is None:
        prev = int(d)
        continue

    if int(d) > prev:
        count += 1

    prev = int(d)

print(count)