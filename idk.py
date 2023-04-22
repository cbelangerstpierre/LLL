import timeit
import math
from sympy import Matrix
from basis import get_basis
from lattice2 import get_lattice2
from lattice import get_lattice
from utils import get_longest_length, get_pairs_count, is_basis
from plot import get_plot
from lll import LLL
from primitive_roots import get_first_primitive, primesfrom2to, testAndMGenerate
from vector_generator import get_vector_generator2, get_vector_generator3
from vector_generator import get_vector_generator
from decimal import Decimal, getcontext


# Q = 2000003
# Q = 

# start = timeit.default_timer()
# gen = get_first_primitive(Q)
# print("Time : " + str(timeit.default_timer() - start))
# start = timeit.default_timer()
# V = get_vector_generator2(Q, gen)
# print("Time : " + str(timeit.default_timer() - start))
# print(V)
# start = timeit.default_timer()
# V = get_vector_generator3(Q, gen)
# print("Time : " + str(timeit.default_timer() - start))
# print(V)
# start = timeit.default_timer()
# index, point = get_lattice2(Q - 1, V)
# print(index)
# print(point)
# print("Time : " + str(timeit.default_timer() - start))
# box_size = Q / math.log(math.log(Q))
# print(box_size)
# chance_outside_box = 1 - (box_size / ((Q - 1) / 2)) ** len(V)
# print(chance_outside_box)
# print(points)
# print(points_sorted)
# print(points_sorted)
# V = get_vector_generator(Q, get_first_primitive(Q))
# print(V)
# num_points, points, points_sorted = get_lattice(Q - 1, V)
# print(points_sorted)


# for Q in map(int, primesfrom2to(10000)[2:]):
#     # start = timeit.default_timer()
#     V = get_vector_generator3(Q, get_first_primitive(Q))
#     # print("Time : " + str(timeit.default_timer() - start))
#     # start = timeit.default_timer()
#     index, point = get_lattice2(Q - 1, V)
#     # print("Time : " + str(timeit.default_timer() - start))
#     if index != 1:
#         print(Q, "=>", index)
Q = 3329
for gen in testAndMGenerate(Q):
    V = get_vector_generator3(Q, gen)
    # print("Time : " + str(timeit.default_timer() - start))
    # start = timeit.default_timer()
    index, point = get_lattice2(Q - 1, V)
    # print("Time : " + str(timeit.default_timer() - start))
    if index != 1:
        print(gen, "=>", index)

# Q = 470206921
# V = get_vector_generator3(Q, get_first_primitive(Q))
# # print("Time : " + str(timeit.default_timer() - start))
# # start = timeit.default_timer()
# index, point = get_lattice2(Q - 1, V)
# # print("Time : " + str(timeit.default_timer() - start))
# print(Q, "=>", index)

# for Q in range(1000, 10000, 10):
#     box_size = Q / math.log(math.log(Q))
#     chance_outside_box = 1 - (box_size / ((Q - 1) / 2)) ** math.floor(math.log(Q))
#     chance_every_point_outside_box = Decimal(chance_outside_box) ** Q
#     print(Q, "=>", str(round(chance_outside_box * 100, 10)) + "%")
#     # print(Q, "=>", float(chance_every_point_outside_box * 100))





# for Q in map(int, primesfrom2to(5000)):
#     if Q < 1500:
#         continue
#     box_size = Q / math.log(math.log(Q))
#     chance_outside_box = 1 - (box_size / ((Q - 1) / 2)) ** math.floor(math.log(Q))
#     V = get_vector_generator3(Q, get_first_primitive(Q))
#     num_points, points, points_sorted = get_lattice(Q - 1, V)
#     total = 0
#     # print(box_size)
#     for point in points_sorted:
#         abs_point = list(map(abs, point))
#         if (max(abs_point)) <= box_size:
#             total += 1
#     print(Q, "=>", str(round(100 - total / len(points_sorted) * 100, 5)) + "%")
#     chance_every_point_outside_box = Decimal(chance_outside_box) ** Q
#     print(Q, "=>", str(round(chance_outside_box * 100, 5)) + "%")
#     # # print(Q, "=>", float(chance_every_point_outside_box * 100))