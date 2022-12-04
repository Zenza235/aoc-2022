from collections import Counter
import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

def get_priority(c: str) -> int:
    return ord(c) - 38 if c.isupper() else ord(c) - 96

total = 0

for i in range(0, len(input), 3):
    r1 = input[i]
    r2 = input[i + 1]
    r3 = input[i + 2]

    dict1 = Counter(r1)
    dict2 = Counter(r2)
    dict3 = Counter(r3)

    commonchar = list((dict1 & dict2 & dict3).elements())

    total += get_priority(commonchar[0])
    

print(total)