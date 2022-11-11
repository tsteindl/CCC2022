import pacman





class Board:
    def __init__(self, size, board_matrix):
        self.size = size
        self.matrix = board_matrix

    def moveLeft(self, pac):
        pac.col = pac.col - 1
        return

    def moveRight(self, pac):
        pac.col = pac.col + 1
        return

    def moveUp(self, pac):
        pac.row = pac.row - 1
        return

    def moveDown(self, pac):
        pac.row = pac.row + 1
        return

    def __str__(self):
        ret = ""
        for line in self.matrix:
            for c in line:
                ret += c + ' '
            ret += '\n'

    def check_pac_on_coin(self, pac: pacman.PacMan):
        if self.check_pac_valid_positions(pac):
            if self.matrix[pac.row][pac.col] == "C":
                self.matrix[pac.row][pac.col] = "0"
                return True
            else:
                return False
        return False

    def check_pac_valid_positions(self, pac):
        if pac.row < 1 or pac.row > self.size or pac.col < 1 or pac.row > self.size:
            print("Error: invalid pacman position!")
            return False
        else:
            return True
