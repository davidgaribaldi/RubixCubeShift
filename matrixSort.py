# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:09:46 2018

@author: davidg
"""

def rotate90(matrix, length):
    fakeMatrix = [[] for _ in range(length)]
    for elem in matrix:
        fakeMatrix[0].insert(0, elem[length-length])
        fakeMatrix[1].insert(0, elem[length-2])
        fakeMatrix[2].insert(0, elem[length-1])
    return fakeMatrix
    
        
    

new_matrix = []    
matrix1 = [[1,2,3], ["a",'b','c'], [7,8,9]]
print(matrix1)
length = len(matrix1)
new_matrix = rotate90(matrix1, length)

print(new_matrix)