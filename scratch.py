from sympy import *

M = Matrix([[2, 1, 8, -4, 5], [0, 4, 1, 6, 3], [1, 3, 1, 1, 0]])
print("Matrix : {} ".format(M))

# Use sympy.rref() method
M_rref = M.rref()
# for ma in list(M_rref[0]):
#     print(ma)
print(M_rref[0].row(0))

print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))
