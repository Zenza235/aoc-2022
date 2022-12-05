import sys

with open(f'{sys.argv[1]}.txt', 'r') as f:
    input = f.read().splitlines()

split = input.index('')
instructions = input[split + 1 : ]
stack_data = input[ : split - 1]
num_stacks = int(input[split - 1].strip()[-1])

sd = [a.split(' ') for a in stack_data]

stacks = []

for s in range(len(sd[0])):
    stack = []
    for i in range(len(sd) - 1, -1, -1):
        str = sd[i][s]
        if str != '':
            stack.append(str[1])

    stacks.append(stack)

print(stacks)

# TODO parsing stacks into respective arrays
# look into condensing stack operations someway
# compare start of test to end of test, find pattern in instruction
# (e.g. elements on top determinable by number of operations done on each stack, etc.)