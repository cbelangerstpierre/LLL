import timeit
from sympy import Matrix
from basis import get_basis
from lattice import get_lattice
from utils import get_longest_length, get_pairs_count, is_basis
from plot import get_plot
from lll import LLL
from primitive_roots import get_first_primitive
from vector_generator import get_vector_generator3


# Q = 11
# V = get_vector_generator3(Q, get_first_primitive(Q))
Q = 101
V = [31, 87]
delta = 0.75
print("Q =", Q)
print("V =", V)
print("Len of V =", len(set(V)))

num_points, points, points_sorted = get_lattice(Q - 1, V)
points_sorted_new = points_sorted.copy()
for point in reversed(points_sorted):
    if tuple(map(lambda x: -x, point)) in points_sorted_new:
        points_sorted_new.remove(point)
print("len points =", len(points_sorted_new))
# print("len points =", len(points_sorted))
print("Points =", points_sorted_new)
# print("Points =", points_sorted)
print("Points sum =", [sum(point) for point in points])
print("Assumed len basis =", len(V) - get_pairs_count(V, Q - 1))
basis = points_sorted_new[:len(V) - get_pairs_count(V, Q - 1)]
start = timeit.default_timer()
if not is_basis(Matrix([[basis[b][a] for b in range(len(basis))] for a in range(len(basis[0]))])):
    basis = get_basis(points_sorted_new, len(V) - get_pairs_count(V, Q - 1))
print("Time taken =", timeit.default_timer() - start)
print("Len of B =", len(basis))
print("Basis =\n" + "\n".join(list(map(str, basis))))
longest_vector, longest_vector_length = get_longest_length(basis)
print("Longest basis vector =", str(longest_vector) + "\nWith a length of", longest_vector_length)
print("Biggest composant of biggest basis vector =", str(max(longest_vector)))
# print("Is really a basis =", is_basis(Matrix([[basis[b][a] for b in range(len(basis))] for a in range(len(basis[0]))])))
reduced_basis = LLL(basis.copy(), delta)
if list(map(tuple, reduced_basis)) != basis:
    print("\nReduced Basis =\n" + "\n".join(list(map(str, reduced_basis))))
    get_plot(Q - 1, V, points, num_points, basis, reduced_basis, show_even=True)
else:
    get_plot(Q - 1, V, points, num_points, basis, show_even=False)