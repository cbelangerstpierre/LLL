import math
import matplotlib.pyplot as plt
import numpy as np


def lattice_plot(Q: int, V: list, show_plot=False) -> dict:
    q_range = (Q - 1) / 2
    # List of starting points, initialized to 0, with length equal to the length of V
    starting_point = [0 for _ in range(len(V))]

    # List of current positions, initialized to 0, with length equal to the length of V
    pos = [0 for _ in range(len(V))]

    # List of lists, where each sublist represents the coordinates of the lattice points in each dimension
    points = [[] for _ in range(len(V))]

    # Function to update the current position in each dimension
    def update_pos():
        for i in range(len(pos)):
            # The position in each dimension is updated by adding the velocity in that dimension and taking the modulus
            new_pos = pos[i] + V[i]
            # print(new_pos)
            if new_pos > q_range:
                new_pos -= Q
            # print(new_pos)
            # print("--------------")
            pos[i] = new_pos

    # Function to calculate the lattice points
    def calculate_lattice():
        num_points = 0
        points_sorted = []
        while pos != starting_point or num_points == 0:
            # Append the current position to the list of points in each dimension
            # print(pos)
            for i in range(len(points)):
                points[i].append(pos[i])
            # print(pos)
                    # pos_to_add = [abs(x) for x in pos]
                    # if pos_to_add not in points_sorted:
            points_sorted.append(tuple(pos))
            # print(points_sorted)
            num_points += 1
            # Update the position in each dimension
            update_pos()
        
        def length(e):
            return np.linalg.norm(np.array(e))
        points_sorted = sorted(points_sorted[1:], key=length)
        return num_points, points_sorted

    # Function to create a 2D plot of the lattice points
    def create_2D_plot(num_points):
        # Set the title of the plot to indicate the velocity vector and the modulus value
        plt.title("Lattice of " + str(V) + " with mod " + str(Q))
        # Add text to the plot indicating the number of points in the lattice
        plt.text(-q_range / 2, -q_range * 1.4, "Number of points=" + str(num_points), horizontalalignment='center')
        # Set the x and y limits of the plot
        plt.xlim(-q_range, q_range)
        plt.ylim(-q_range, q_range)
        # Plot the lattice points as dots on the plot
        plt.plot(points[0], points[1], 'o')
        # Display the plot
        plt.axis('square')
        plt.show()

    # Function to create a 3D plot of the lattice points
    def create_3D_plot():
        # Create a figure with a set size
        fig = plt.figure(figsize=(5, 5))
        # Add a 3D subplot to the figure
        ax = fig.add_subplot(projection='3d')

        # Set the x, y, and z limits of the 3D plot
        ax.set_xlim3d(-q_range, q_range)
        ax.set_ylim3d(-q_range, q_range)
        ax.set_zlim3d(-q_range, q_range)

        # Plot the lattice points as a scatter plot
        ax.scatter(points[0], points[1], points[2])
        # Display the plot
        plt.show()

    # Calculate the lattice based on the values of Q and V
    num_points, points_sorted = calculate_lattice()

    if show_plot:
        # If the length of V is 2, create a 2D plot
        if len(V) == 2:
            create_2D_plot(num_points)

        # If the length of V is 3, create a 3D plot
        elif len(V) == 3:
            create_3D_plot()

    return {"Q": Q, "V": V, "num_points": num_points, "points": points, "sorted": points_sorted}


if __name__ == '__main__':
    print(lattice_plot(23, [2, 3], True)["sorted"])
