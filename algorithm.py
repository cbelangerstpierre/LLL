from basis import get_basis
from lattice import get_lattice
from plot import get_plot
from lll import LLL

Q = 11
V = [2, 4, 7]

delta = 0.75
# print(len(set(V)))

num_points, points, points_sorted = get_lattice(Q, V)
basis = get_basis(points_sorted, len(set(V)))
# print(len(basis))
# print(points_sorted)
# print("_____________________")
print("Basis =\n" + "\n".join(list(map(str, basis))))
reduced_basis = LLL(basis.copy(), delta)
if list(map(tuple, reduced_basis)) != basis:
    print("\nReduced Basis =\n" + "\n".join(list(map(str, reduced_basis))))
    get_plot(Q, V, points, num_points, basis, reduced_basis)
else:
    get_plot(Q, V, points, num_points, basis)


"""
* Observations :

1. The number of vectors in the lattice will not be equal to the number of components in the vector generator,
   but the number of *Different components, example. the vector : [2, 3, 5, 3] will have only 3 vectors in the basis.
   (Not always), tested other Q and V combinations for which it wasn't the case, no repetition and it still had less vectors

2. Every time a component is repeated in the vector generator,
   The components in the vectors of the basis will repeat at the exact same places
   Example : the vector [3, 3, 2] will give the basis : [[3, 3, 2], [910, 910, -2727]]
   Example 2 : The vector [1, 5, 3, 1, 4] will give the basis : [[1, 5, 3, 1, 4], [13, 8, -18, 13, -5], [19, -19, 0, 19, 19], [10, -7, 30, 10, -17]]
   This is the case even after the LLL reduction, which makes sense because it reduces a vector by the other vectors,
   which are also repeating their components at the same place.

3. Q = 125, V = [4, 23]
   Basis = [(-10, 5), (7, 9)]
   abs(floor(125 / 23)) = 5
   125 % 23 = 10
   ?????
"""
