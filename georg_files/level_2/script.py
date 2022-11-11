import parser

level = 'level2'
subtask = '1'
n = 0
board_matrix = []


def print_board_matrix(tofile: bool):
    filename = level + '_' + subtask
    with open(filename, 'w') as f:
        for line in board_matrix:
            for c in line:
                f.write(c)
                print(c, end=' ')
            f.write('\n')
            print()


parser.parsefile_level1('../../level_1/level1_1.in')
print_board_matrix(False)
