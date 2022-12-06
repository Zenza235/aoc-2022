import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read()

print(input)

