with open('input.txt', 'r') as input:
    data = list(map(int, input.read().split(',')))

fule_list = [sum([
    abs(v - d) * (abs(v - d) + 1) / 2 for d in data
]) for v in range(max(data))]

print(f'{min(fule_list)}')

"""
1,2,3,4,5,6,7,8,9,10
# # # # # # # # # # 10
  # # # # # # # # # 9
    # # # # # # # # 8
      # # # # # # # 7
        # # # # # # 6
          # # # # # 5
            # # # # 4
              # # # 3
                # # 2
                  # 1
                    0
"""