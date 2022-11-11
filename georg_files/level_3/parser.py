import ghost


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

        board_matrix = []
        for i in range(n):
            board_row = (f.readline().rstrip())
            board_matrix.append(board_row)

        position = f.readline()
        position = position.split()
        pac_row = int(position[0])-1
        pac_col = int(position[1])-1

        sequence_len = int(f.readline())
        seq = f.readline()

    return n, board_matrix, pac_row, pac_col, sequence_len, seq



def parsefile_level3(file: str):
    with open(file) as f:
        n = int(f.readline())

        board_matrix = []
        for i in range(n):
            board_row = (f.readline().rstrip())
            board_matrix.append(board_row)

        position = f.readline()
        position = position.split()
        pac_row = int(position[0])-1
        pac_col = int(position[1])-1

        sequence_len = int(f.readline())
        seq = f.readline()

        n_ghosts = int(f.readline())
        ghosts = []
        for i in range(n_ghosts):
            position = f.readline()
            position = position.split()
            g_seq_len = int(f.readline())
            g_seq = f.readline().rstrip()
            ghosts.append(ghost.Ghost(int(position[0])-1, int(position[1])-1, g_seq))


    return n, board_matrix, pac_row, pac_col, sequence_len, seq, n_ghosts, ghosts


test = parsefile_level3('in/level3_example.in')
print("")
