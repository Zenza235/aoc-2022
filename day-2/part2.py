# A == rock (1)       X == lose
# B == paper (2)       Y == draw
# C == scissors (3)   Z == win

# Win == 6
# Draw == 3
# Lose == 0

dict = {
    'A X' : 0 + 3, # lose
    'A Y' : 3 + 1, # draw
    'A Z' : 6 + 2, # win
    'B X' : 0 + 1, # lose
    'B Y' : 3 + 2, # draw
    'B Z' : 6 + 3, # win
    'C X' : 0 + 2, # lose
    'C Y' : 3 + 3, # draw
    'C Z' : 6 + 1 # win
}

import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

total = 0

for a in input:
    total += dict[a]

print(total)