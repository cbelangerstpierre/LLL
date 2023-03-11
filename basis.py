import numpy as np
from sympy import Matrix
import timeit
from utils import is_combination

def get_basis(points_sorted: list, length: int) -> list:
    basis = [points_sorted[0]]
    start = timeit.default_timer()
    for index, point in enumerate(points_sorted):
            if not is_combination(Matrix([[basis[b][a] for b in range(len(basis))] + [point[a]] for a in range(len(basis[0]))]).rref()[0]):
                basis.append(point)
                print(index)
                if len(basis) == length:
                    break
    print("Time to calculate the basis is :", timeit.default_timer() - start)
    return basis



# To understand line 6 :
# for i in range(M.rows):
#     row = M.row(i)
#     if all(num == 0 for num in row[:-1]) and row[-1] != 0:
#         return False
# return True


# To understand line 16 :
# matrice = []
# for a in range(len(basis[0])):
#     liste = []
#     for b in range(len(basis)):
#         liste.append(basis[b][a])
#     matrice.append(liste + [point[a]])
# print(matrice)
