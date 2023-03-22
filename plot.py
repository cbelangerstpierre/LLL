import matplotlib.pyplot as plt
import numpy as np

def get_plot(Q, V, points, num_points, basis, reduced_basis=None):

    q_range = Q / 2

    # Function to create a 2D plot of the lattice points
    def create_2D_plot(num_points):
        print(points)
        # Set the title of the plot to indicate the velocity vector and the modulus value
        plt.title("Lattice of " + str(V) + " with mod " + str(Q))
        # Add text to the plot indicating the number of points in the lattice
        plt.text(-q_range / 2, -q_range * 1.4, "Number of points=" + str(num_points), horizontalalignment='center')
        # Set the x and y limits of the plot
        plt.xlim(-q_range, q_range)
        plt.ylim(-q_range, q_range)
        # Plot the lattice points as dots on the plot
        # evens = points[::2]
        #  = points[1::2]
        green = plt.scatter(points[0][::2], points[1][::2], color="g")
        blue = plt.scatter(points[0][1::2], points[1][1::2], color="b")
        # plt.legend((blue, red), ("Pair", "Impair"), loc="center")
        red = plt.arrow(0, 0, basis[0][0], basis[0][1], color="r", label="basis")
        if len(basis) > 1:
            plt.arrow(0, 0, basis[1][0], basis[1][1], color="r")
        if reduced_basis:
            plt.arrow(0, 0, reduced_basis[0][0], reduced_basis[0][1], color="b", label="LLL")
            if len(reduced_basis) > 1:
                plt.arrow(0, 0, reduced_basis[1][0], reduced_basis[1][1], color="b")

        ax = plt.subplot(111)
        # Shrink current axis by 20%
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend((green, blue, red), ("Pair", "Impair", "Basis"), loc='center left', bbox_to_anchor=(1, 0.5))

        # Display the plot
        plt.axis('square')
        ax.axis("square")


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
        ax.scatter(points[0][::2], points[1][::2], points[2][::2], color="g")
        ax.scatter(points[0][1::2], points[1][1::2], points[2][1::2], color="b")
        ax.plot([0, 0], [0, 0])
        # ax.plot([0, basis[0][0]], [0, basis[0][1]], zs=[0, basis[0][2]])
        # ax.plot([0, basis[1][0]], [0, basis[1][1]], zs=[0, basis[1][2]])
        # if len(basis) > 2:
        #     ax.plot([0, basis[2][0]], [0, basis[2][1]], zs=[0, basis[2][2]])
        # Display the plot
        plt.show()

    # If the length of V is 2, create a 2D plot
    if len(V) == 2:
        create_2D_plot(num_points)

    # If the length of V is 3, create a 3D plot
    elif len(V) == 3:
        create_3D_plot()
