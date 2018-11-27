# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:09:46 2018

@author: davidg
"""


def rotate90(matrix):
    length = 0
    length = len(matrix)
    n = 0
    fakeMatrix = [[] for _ in range(length)]
    for n in range(length):
        for elem in matrix:
            fakeMatrix[n].insert(0, elem[n])
    return fakeMatrix


new_matrix = []
matrix1 = [[1, 2, 3, 4], ["a", 'b', 'c', 'd'], [7, 8, 9, 10], ['as', 'sd', 'pl', 'ok']]
print(matrix1)
new_matrix = rotate90(matrix1)

print(new_matrix)
