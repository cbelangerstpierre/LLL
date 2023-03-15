import math
import numpy as np


def get_lattice2(Q: int, V: list) -> tuple:
    q_range = Q / 2
    # List of starting points, initialized to 0, with length equal to the length of V
    starting_point = [0 for _ in range(len(V))]

    # Change the commented line to switch between every integers and only odds, also change line 23
    pos = [0 for _ in range(len(V))]

    # Function to update the current position in each dimension
    def update_pos():
        for i in range(len(pos)):
            # The position in each dimension is updated by adding the velocity in that dimension and taking the modulus
            # Remove the * 2 to get every integers, put it to only have odds
            new_pos = pos[i] + V[i]
            if new_pos > q_range:
                new_pos -= Q
            pos[i] = new_pos


    def dedede():
        i = 0
        while pos != starting_point or i == 0:
            if i != 0 and i % 2 == 1:
                abs_point = list(map(abs, pos.copy()))
                if (max(abs_point)) <= (Q / math.log(math.log(Q))):
                    return (i, pos)
            i += 1
            update_pos()

    # Calculate the lattice based on the values of Q and V
    index, point = dedede()
    return (index, point)

if __name__ == '__main__':
    print(get_lattice2(23, [2, 3]))
