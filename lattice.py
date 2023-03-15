import numpy as np


def get_lattice(Q: int, V: list) -> tuple:
    q_range = Q / 2
    # List of starting points, initialized to 0, with length equal to the length of V
    starting_point = [0 for _ in range(len(V))]

    # List of current positions, initialized to 0, with length equal to the length of V

    # Change the commented line to switch between every integers and only odds, also change line 23
    pos = [0 for _ in range(len(V))]
    # pos = V.copy()

    # List of lists, where each sublist represents the coordinates of the lattice points in each dimension
    points = [[] for _ in range(len(V))]

    # Function to update the current position in each dimension
    def update_pos():
        for i in range(len(pos)):
            # The position in each dimension is updated by adding the velocity in that dimension and taking the modulus
            # Remove the * 2 to get every integers, put it to only have odds
            new_pos = pos[i] + V[i]
            if new_pos > q_range:
                new_pos -= Q
            pos[i] = new_pos

    # Function to calculate the lattice points
    def calculate_lattice():
        num_points = 0
        points_sorted = []
        while pos != starting_point or num_points == 0:
            # Append the current position to the list of points in each dimension
            for i in range(len(points)):
                points[i].append(pos[i])
            points_sorted.append(tuple(pos))
            num_points += 1
            # Update the position in each dimension
            update_pos()
        
        def length(e):
            return np.linalg.norm(np.array(e))
        # Add [1:] to have every integers
        points_sorted = sorted(points_sorted[1:], key=length)
        return num_points, points_sorted

    # Calculate the lattice based on the values of Q and V
    num_points, points_sorted = calculate_lattice()
    return (num_points, points, points_sorted)


if __name__ == '__main__':
    print(get_lattice(23, [2, 3], True))
