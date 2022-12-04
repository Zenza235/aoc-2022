import sys
import re

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

overlap_total = 0

for a in input:
    temp = re.split('-|,', a)
    nums = [int(s) for s in temp]

    if (nums[3] - nums[0]) * (nums[2] - nums[1]) <= 0:
        overlap_total += 1

print(overlap_total)