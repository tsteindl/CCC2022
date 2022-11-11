from os import listdir
from os.path import isfile, join

def parse_file(file_name: str):
    matrix = []
    n = 0
    p_row = 0
    p_col = 0
    seq_len = 0
    mvt_seq = []
    matrix = []
    with open("in/" + file_name) as f:
        lines = f.readlines()
    # for line in lines:
    #     line = line.rstrip()
    lines = list(map(lambda l: l.rstrip(), lines))
    matrix = []
    length = len(lines)
    for i, line in enumerate(lines):
        if i == 0:
            n = int(line)
            continue
        if i == length - 3:
            curr_line = list(line.split(" "))
            p_row = int(curr_line[0]) - 1
            p_col = int(curr_line[1]) - 1
            continue
        if i == length - 2:
            seq_len = int(line)
            continue
        if i == length - 1:
            mvt_seq = list(line.rstrip())[:seq_len]
            continue
        # matrix.append(list(line.rstrip()))
    matrix_input = lines[1:-3]
    for i in range(n):
        matrix.append(list(matrix_input[i].rstrip()))
    return n, matrix, p_row, p_col, seq_len, mvt_seq

def search_coins(n, matrix, p_row, p_col, seq_len, mvt_seq):
    curr_pos = [p_row, p_col]
    cnt = 0
    for i in range(seq_len):
        dir = mvt_seq[i]
        if (dir == "L"):
            curr_pos[1] = curr_pos[1] - 1
        if (dir == "R"):
            curr_pos[1] = curr_pos[1] + 1
        if (dir == "U"):
            curr_pos[0] = curr_pos[0] - 1
        if (dir == "D"):
            curr_pos[0] = curr_pos[0] + 1
        print("moving: " + dir + " next idx: " + str(curr_pos) + " with found coins: " + str(cnt))
        if matrix[curr_pos[0]][curr_pos[1]] == "C":
            matrix[curr_pos[0]][curr_pos[1]] = "0"
            cnt += 1

    return cnt



onlyfiles = [f for f in listdir("in") if isfile(join("in", f))]
for file in onlyfiles:
    print("\nparsing file " + file)
    (n, matrix, p_row, p_col, seq_len, mvt_seq) = parse_file(file)
    cnt = search_coins(*(n, matrix, p_row, p_col, seq_len, mvt_seq))
    with open("out/" + file + ".out", 'w') as f:
        f.write(str(cnt))

