import sys

def find_marker(s: str, num: int) -> int:
    for i in range(0, len(s) - num):
        a = s[i : i + num]

        arr = []

        for c in a:
            if c not in arr:
                arr.append(c)

        if len(arr) == num:
            return i + num

if __name__ == '__main__':
    with open(f'{sys.argv[1]}.txt', 'r') as f:
        input = f.read()

    print(find_marker(input, 14))