with open('level1_1.in') as f:
    lines = f.readlines()


matrix = []
for i, line in enumerate(lines):
    if i == 0:
        n = line
        continue
    matrix.append(list(line.rstrip()))



#for i in range(n):
#    matrix[i] = list(lines[i])


print(matrix)

