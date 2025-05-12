#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != 0:
                    print(" ", end="")
                print("{:d}".format(matrix[i][j]), end="")
            print("")
