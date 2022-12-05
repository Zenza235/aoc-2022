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

def do_ins(num_move: int, start: list, end: list) -> list:
    for i in range(num_move):
        val = start.pop(len(start) - 1)
        end.append(val)

for ins in instructions:
    words = ins.split(' ')
    move_amt = int(words[1])
    start_stack = int(words[3])
    end_stack = int(words[5])

    do_ins(move_amt, stacks[start_stack - 1], stacks[end_stack - 1])

print(stacks)

result = ''

for stack in stacks:
    result += stack[len(stack) - 1]

print(result)