# A == rock        X == rock (1 pts)
# B == paper       Y == paper (2 pts)
# C == scissors    Z == scissors (3 pt)

# Win == 6
# Draw == 3
# Lose == 0

import sys

dict = {
    'A X' : 4, # tie
    'A Y' : 8, # win
    'A Z' : 3, # loss
    'B X' : 1, # loss
    'B Y' : 5, # tie
    'B Z' : 9, # win
    'C X' : 7, # win
    'C Y' : 2, # loss
    'C Z' : 6 # tie
}

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

total = 0

for a in input:
    total += dict[a]

print(total)
