# part 2
import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

curr_num = 0
m = [0, 0, 0] # m[0], m[1], m[2] (descending order)

for a in input:
    if a == '':
        # max = curr_num if curr_num > max else max
        if curr_num > m[0]:
            m[2] = m[1]
            m[1] = m[0]
            m[0] = curr_num
        elif curr_num > m[1]:
            m[2] = m[1]
            m[1] = curr_num
        elif curr_num > m[2]:
            m[2] = curr_num
        curr_num = 0
    else:
        curr_num += int(a)

print(m)
print(sum(m))