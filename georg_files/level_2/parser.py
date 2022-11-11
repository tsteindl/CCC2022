def parsefile_level1(file: str):
    with open(file) as f:
        n = int(f.readline())
        lines = f.readlines()
    board_matrix = []
    for line in lines:
        board_matrix.append(list(line.split()))

    return n, board_matrix


def parsefile_level2(file: str):
    with open(file) as f:
        n = int(f.readline())
        lines = []
        for i in range(n):
            lines.append(f.readline())
        position = f.readline()
        position = position.split()
        pac_row = int(position[0])-1
        pac_col = int(position[1])-1

        sequence_len = int(f.readline())
        seq = f.readline()

    board_matrix = []
    for line in lines:
        board_matrix.append(line.rsplit())

    return n, board_matrix, pac_row, pac_col, sequence_len, seq
