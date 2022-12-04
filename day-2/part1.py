# A == rock        Y == paper (2 pts)
# B == paper       Z == scissors (3 pts)
# C == scissors    X == rock (1 pt)

# Win == 6
# Draw == 3
# Lose == 0

import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

print(input)