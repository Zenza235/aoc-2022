# part 1
import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

curr_num = 0
max = 0

for a in input:
    if a == '':
        max = curr_num if curr_num > max else max
        curr_num = 0
    else:
        curr_num += int(a)

print(max)