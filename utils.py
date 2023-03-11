import numpy as np
from sympy import Matrix


def is_combination(M: Matrix) -> bool:
    return False if any(all(num == 0 for num in row[:-1]) and row[-1] != 0 for i in range(M.rows) if (row := M.row(i))) else True

def is_basis(M: Matrix) -> bool:
    # print(M.cols)
    return len(M.T.rref()[1]) == M.cols

def get_pairs_count(arr, n):
    unordered_map = {}
    count = 0
    for i in range(len(arr)):
        if n - arr[i] in unordered_map:
            count += unordered_map[n - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count

def get_longest_length(B):
    longest = None
    length = 0
    for vector in B:
        v_length = np.linalg.norm(np.array(vector))
        if v_length > length:
            length = v_length
            longest = vector
    return (longest, length)