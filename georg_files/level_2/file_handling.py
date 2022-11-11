from os import listdir
from os.path import isfile, join


def get_in_files():
    return [f for f in listdir("in") if isfile(join("in", f))]


def print_to_file(file, output):
    with open("out/" + file + ".out", 'w') as f:
        f.write(str(output))
