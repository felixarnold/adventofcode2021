with open('input.txt','r') as input:
    data = [[[
        v for v in patterns.split()
                ] for patterns in line.split('|')
            ] for line in input.read().split('\n')
        ]

"""
Segments

  0 0
1     2
1     2
  3 3
4     5
4     5
  6 6

Digint -> Number of segments
0 -> 6
1 -> 2
2 -> 5
3 -> 5
4 -> 4
5 -> 5
6 -> 6
7 -> 3
8 -> 7
9 -> 6

Segment count distribution
2 segments x1
3 segments x1
4 segments x1
5 segments x3
6 segments x3
7 segments x1

"""

total = 0

for d in data:
    digit_struct = {}

    d[0].sort(key=len)
    digits = {
        ''.join(sorted(d[0][0])): '1',
        ''.join(sorted(d[0][2])): '4',
        ''.join(sorted(d[0][1])): '7',
        ''.join(sorted(d[0][9])): '8'
    }

    zero = '#'
    one = d[0][0]
    two = '#'
    three = '#'
    four = d[0][2]
    five = '#'
    six = '#'
    seven = d[0][1]
    eight = d[0][9]
    nine = '#'
    zero_six_nine = d[0][6:9]
    two_three_five = d[0][3:6]

    digit_struct[0] = (set(seven) - set(one)).pop()

    for p in two_three_five:
        if one[0] in p and one[1] in p:
            three = p
            digits[''.join(sorted(p))] = '3'
            two_three_five.remove(p)
            break

    digit_struct[1] = (set(four) - set(three)).pop()
    digit_struct[3] = (set(four) - set(one) - set(digit_struct[1])).pop()

    for p in two_three_five:
        if digit_struct[1] in p:
            five = p
            digits[''.join(sorted(p))] = '5'
            continue
        two = p
        digits[''.join(sorted(p))] = '2'

    for p in zero_six_nine:
        if one[0] not in p or one[1] not in p:
            six = p
            digits[''.join(sorted(p))] = '6'
            continue
        if digit_struct[3] in p:
            nine = p
            digits[''.join(sorted(p))] = '9'
            continue
        zero = p
        digits[''.join(sorted(p))] = '0'

    output = str()
    for p in d[1]:
        output += digits[''.join(sorted(p))]
    total += int(output)

print(total)