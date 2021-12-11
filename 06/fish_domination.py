with open('input.txt', 'r') as input:
    data = input.read().split(',')

fishies = [0]*9

for fish in data:
    fishies[int(fish)] += 1


def day_in_a_life_of_fishies(fishies: list[int]):
    tomorrows_fishies = [0]*9
    for i, fish_count in enumerate(fishies):
        tomorrows_fishies[i-1] = fish_count

    tomorrows_fishies[6] += tomorrows_fishies[8]

    return tomorrows_fishies


for i in range(256):
    fishies = day_in_a_life_of_fishies(fishies)

print(sum(fishies))