import timeit
from sympy import Matrix
from basis import get_basis
from lattice2 import get_lattice2
from utils import get_longest_length, get_pairs_count, is_basis
from plot import get_plot
from lll import LLL
from primitive_roots import get_first_primitive
from vector_generator import get_vector_generator2, get_vector_generator3
from vector_generator import get_vector_generator


Q = 2000003

start = timeit.default_timer()
gen = get_first_primitive(Q)
print("Time : " + str(timeit.default_timer() - start))
# start = timeit.default_timer()
# V = get_vector_generator2(Q, gen)
# print("Time : " + str(timeit.default_timer() - start))
# print(V)
start = timeit.default_timer()
V = get_vector_generator3(Q, gen)
print("Time : " + str(timeit.default_timer() - start))
print(V)
start = timeit.default_timer()
index, point = get_lattice2(Q - 1, V)
print(index)
print(point)
print("Time : " + str(timeit.default_timer() - start))
# print(points)
# print(points_sorted)
# print(points_sorted)
# V = get_vector_generator(Q, get_first_primitive(Q))
# print(V)
# num_points, points, points_sorted = get_lattice(Q - 1, V)
# print(points_sorted)
