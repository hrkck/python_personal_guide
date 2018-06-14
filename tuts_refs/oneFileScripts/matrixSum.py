'''
Created on May 31, 2016

@author: hrkucuk
'''


def sumMatrix(matrix):

    result = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            result += matrix[row][column]
    print("Sum of the elementst of the Matrix is %d" % result)


def printMatrix(matrix):
    print("   ", end='')
    for column in range(len(matrix)):
        print("%d.\t" % column, end='')
    print()
    for row in range(len(matrix)):
        print("%d. " % (row + 1), end='')
        for column in range(len(matrix[row])):
            print("%d\t" % matrix[row][column], end='')
        print()


matrix = [[2, 3, 5], [1, 3, 4], [56, 7, 1]]

sumMatrix(matrix)
printMatrix(matrix)
