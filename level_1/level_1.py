from typing import List

n = 0
matrix = []

def parse_file(file : str):
    global matrix
    global n
    with open(file) as f:
        lines = f.readlines()
    matrix = []
    for i, line in enumerate(lines):
        if i == 0:
            n = line
            continue
        matrix.append(list(line.rstrip()))

def find_coins(matrix : List[List[str]]) -> int:
    cnt = 0
    for line in matrix:
        for i in line:
            if i == "C":
                cnt += 1
    return cnt


parse_file('level1_5.in')

n = find_coins(matrix)

with open('level1_5.out', 'w') as f:
    f.write(str(n))


# print(matrix)
print(n)
