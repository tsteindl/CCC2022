def parse_file(file_name: str):
    matrix = []
    n = 0
    p_row = 0
    p_col = 0
    seq_len = 0
    mvt_seq = []
    matrix = []
    with open(file_name) as f:
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
            p_row = int(curr_line[0])
            p_col = int(curr_line[1])
            continue
        if i == length - 2:
            seq_len = int(line)
            continue
        if i == length - 1:
            mvt_seq.append(list(line.rstrip()))
            continue
        matrix.append(list(line.rstrip()))
    return n, matrix, p_row, p_col, seq_len, mvt_seq


(n, matrix, p_row, p_col, seq_len, mvt_seq) = parse_file("in/level2_1.in")
print((n, matrix, p_row, p_col, seq_len, mvt_seq))
