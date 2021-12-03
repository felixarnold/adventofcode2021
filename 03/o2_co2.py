with open('input.txt', 'r') as input:
    data = input.read().split('\n')

o2 = 0
co2 = 0

def filter(data: list, pos: int, l: int, pri: int, sec) -> int:
    count = 0
    bit = [[], []]

    for d in data:
        if d[pos] == '1':
            count += 1
            bit[1].append(d)
            continue
        bit[0].append(d)


    if count >= l / 2:
        if len(bit[pri]) == 1:
            return int(bit[pri][0], 2)

        return filter(bit[pri], pos + 1, len(bit[pri]), pri, sec)

    if count < l / 2:
        if len(bit[sec]) == 1:
            return int(bit[sec][0], 2)

        return filter(bit[sec], pos + 1, len(bit[sec]), pri, sec)


o2 = filter(data, 0, len(data), 1, 0)
co2 = filter(data, 0, len(data), 0, 1)

print(o2 * co2)