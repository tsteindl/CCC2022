import parser
import file_handling
import board
import pacman


def function_level2(filename):
    n, board_matrix, pac_row, pac_col, sequence_len, seq = parser.parsefile_level2(filename)
    b = board.Board(n, board_matrix)
    pac = pacman.PacMan(pac_row, pac_col)

    coins = 0

    if b.check_pac_on_coin(pac):
        coins += 1

    for command in seq:
        if command == "L":
            b.moveLeft(pac)
        elif command == "R":
            b.moveRight(pac)
        elif command == "U":
            b.moveUp(pac)
        elif command == "D":
            b.moveDown(pac)
        else:
            print("Error: command")

        if b.check_pac_on_coin(pac):
            coins += 1

    return coins

# file_handling.print_to_file('out/test.out', output=str(coins))


for f in file_handling.get_in_files():
    c = function_level2('in/'+f)
    print(f)
    print(c)
