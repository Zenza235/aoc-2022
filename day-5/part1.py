import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

split = input.index('')
instructions = input[split + 1 : ]
stack_data = input[ : split - 1]
num_stacks = input[split - 1].strip()[-1]

sd = [a.strip().split(' ') for a in stack_data]

# TODO parsing stacks into respective arrays
# look into condensing stack operations someway
# compare start of test to end of test, find pattern in instruction
# (e.g. elements on top determinable by number of operations done on each stack, etc.)