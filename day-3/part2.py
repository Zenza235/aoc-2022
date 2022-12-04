import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

def get_priority(c: str) -> int:
    return ord(c) - 38 if c.isupper() else ord(c) - 96