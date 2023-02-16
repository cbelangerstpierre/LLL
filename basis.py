from lattice_plot import lattice_plot
from sympy import *
import timeit
from lll import LLL

def get_basis(Q: int, V: tuple, delta=0.75, show_plot=False) -> dict:
    def is_combination(M: Matrix) -> bool:
        return False if any(all(num == 0 for num in row[:-1]) and row[-1] != 0 for i in range(M.rows) if (row := M.row(i))) else True

    # start = timeit.default_timer()
    points = lattice_plot(Q, V, show_plot=show_plot)["sorted"]
    basis = [V]


    for point in points:
        if not is_combination(Matrix([[basis[b][a] for b in range(len(basis))] + [point[a]] for a in range(len(basis[0]))]).rref()[0]):
            basis.append(point)
            if len(basis) == len(V):
                break
    # print("Time:", timeit.default_timer() - start)
    return {"basis": basis, "lll": LLL(basis, delta)}

print(get_basis(1001, (7, 17, 53, 29)))

# To understand line 16 :
# matrice = []
# for a in range(len(basis[0])):
#     liste = []
#     for b in range(len(basis)):
#         liste.append(basis[b][a])
#     matrice.append(liste + [point[a]])
# print(matrice)

# To understand line 6 :
# for i in range(M.rows):
#     row = M.row(i)
#     if all(num == 0 for num in row[:-1]) and row[-1] != 0:
#         return False
# return True