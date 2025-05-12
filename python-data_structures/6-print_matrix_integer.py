#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")
    else:
        for i in range(len(matrix)):
                print("{:d} {:d} {:d}".format(*matrix[i]))
