import timeit
from sympy import Matrix
from basis import get_basis
from lattice import get_lattice
from utils import get_longest_length, get_pairs_count, is_basis
from plot import get_plot
from lll import LLL
from primitive_roots import get_first_primitive
from vector_generator import get_vector_generator


# Q = 163
# V = get_vector_generator(Q, get_first_primitive(Q))
Q = 127
V = [23, 27, 67]
delta = 0.75
print("Q =", Q)
print("V =", V)
print("Len of V =", len(set(V)))

num_points, points, points_sorted = get_lattice(Q, V)
points_sorted_new = points_sorted.copy()
for point in reversed(points_sorted):
    if tuple(map(lambda x: -x, point)) in points_sorted_new:
        points_sorted_new.remove(point)
print("len points =", len(points_sorted_new))
# print("len points =", len(points_sorted))
print("Points =", points_sorted_new)
# print("Points =", points_sorted)
print("Points sum =", [sum(point) for point in points])
print("Assumed len basis =", len(V) - get_pairs_count(V, Q))
basis = points_sorted_new[:len(V) - get_pairs_count(V, Q)]
start = timeit.default_timer()
if not is_basis(Matrix([[basis[b][a] for b in range(len(basis))] for a in range(len(basis[0]))])):
    basis = get_basis(points_sorted_new, len(V) - get_pairs_count(V, Q))
print("Time taken =", timeit.default_timer() - start)
print("Len of B =", len(basis))
print("Basis =\n" + "\n".join(list(map(str, basis))))
longest_vector, longest_vector_length = get_longest_length(basis)
print("Longest basis vector =", str(longest_vector) + "\nWith a length of", longest_vector_length)
print("Is really a basis =", is_basis(Matrix([[basis[b][a] for b in range(len(basis))] for a in range(len(basis[0]))])))
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
30,5s
3. Q = 125, V = [4, 23]
   Basis = [(-10, 5), (7, 9)]
   abs(floor(125 / 23)) = 5
   125 % 23 = 10
   ?????



   WOAHHH
   si une composante plus une autre = une autre composante, alors dans la base aussi
"""
