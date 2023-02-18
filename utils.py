import numpy as np


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