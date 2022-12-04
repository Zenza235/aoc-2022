# 52 unique items (a-z, A-Z)
# each rucksack has equal number of items
# find unique char in each pair of rucksacks
# priorities: a-z => 1-26, A-Z => 27-52

# one method
# PmmdzqPrV + vPwwTWBwg
# search comp2 for each char in comp1
# shit efficiency

import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

total = 0

for a in input:
    comp1 = a[0 : int(len(a) / 2)]
    comp2 = a[int(len(a) / 2) : ]
    for c in comp2:
        if c in comp1:
            total += ord(c) - 38 if c.isupper() else ord(c) - 96
            break
    
print(total)