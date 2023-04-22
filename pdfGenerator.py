from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import timeit
from sympy import Matrix
from basis import get_basis
from lattice import get_lattice
from utils import get_longest_length, get_pairs_count, is_basis
from plot import get_plot
from lll import LLL
from primitive_roots import get_first_primitive, primesfrom2to
from vector_generator import get_vector_generator3

# plt.rcParams["figure.figsize"] = [7.00, 7.00]
plt.rcParams["figure.autolayout"] = True

for Q in map(int, primesfrom2to(1000)[4:]):
    fig = plt.figure()
    print(Q)
    V = get_vector_generator3(Q, get_first_primitive(Q))[:2]
    print(V)
    num_points, points, points_sorted = get_lattice(Q - 1, V)
    points_sorted_new = points_sorted.copy()
    for point in reversed(points_sorted):
        if tuple(map(lambda x: -x, point)) in points_sorted_new:
            points_sorted_new.remove(point)
    basis = points_sorted_new[:len(V) - get_pairs_count(V, Q - 1)]
    if not is_basis(Matrix([[basis[b][a] for b in range(len(basis))] for a in range(len(basis[0]))])):
        basis = get_basis(points_sorted_new, len(V) - get_pairs_count(V, Q - 1))
    fig = get_plot(Q - 1, V, points, num_points, basis, show_even=True)

# fig1 = plt.figure()
# plt.plot([2, 1, 7, 1, 2], color='red', lw=5)

# fig2 = plt.figure()
# plt.plot([3, 5, 1, 5, 3], color='green', lw=5)


def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    print(fig_nums)
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()

filename = "multi2.pdf"
save_multi_image(filename)