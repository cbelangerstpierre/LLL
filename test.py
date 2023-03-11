from lattice import get_lattice
from plot import get_plot
from primitive_roots import testAndMGenerate, primesfrom2to
from vector_generator import get_vector_generator

for prime in primesfrom2to(100)[2:]:
    Q = int(prime)
    roots = testAndMGenerate(Q)
    # for root in roots:
    vector = get_vector_generator(Q, roots[0])
    new_q = Q - 1
    print("Q =", Q, "- V =", vector, "- Len of V =", len(vector), "- len of B will be", len(set(map(lambda x: abs(x - new_q) if x > new_q / 2 else x, vector))))
        # print(vector)
        # num_points, points, points_sorted = get_lattice(Q - 1, vector)
        # print(points_sorted)
        # print(points)
        # get_plot(Q - 1, vector, points, num_points, None)

    print("-------------")
    # print("-------------\n-------------------------------\n------------------------\n---------------------")

# V = get_vector_generator(Q, roots[0])



# print("----------------")
# print(roots)
