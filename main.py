import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def combined_focal_length(f1, f2, d):
    return 1 / (1/f1 + 1/f2 - d/(f1*f2))

def EFDs_given_d(d, ft_values, fk_range):
    X, Y = np.meshgrid(ft_values, fk_range)
    Z = np.array([[combined_focal_length(fk, ft, d) for ft in ft_values] for fk in fk_range])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('EFD of tunable lens (mm)')
    ax.set_ylabel('Known focal length (mm)')
    ax.set_zlabel('Measured EFD at output (mm)')
    ax.set_title(f'Interlens d = {d}mm')
    
    plt.show(block=False)  # Display the plot without blocking the execution

def EFDs_given_fk_d(fk, d, ft_values):
    EFD_output = [combined_focal_length(fk, ft, d) for ft in ft_values]

    plt.figure()
    plt.plot(ft_values, EFD_output)
    plt.xlabel('EFD of tunable lens (mm)')
    plt.ylabel('Measured EFD at output (mm)')
    plt.title(f'Interlens d = {d}mm, Known focal length = {fk}mm')
    plt.grid(True)
    plt.show(block=False)  # Display the plot without blocking the execution

def main():
    d = 50  # Distance between Lk and Lt in mm
    ft_values = np.linspace(999, 100, 100)  # Focal lengths of the tunable lens in mm
    fk_range = np.linspace(10, 150, 100)  # Range of known focal lengths in mm

    EFDs_given_d(d, ft_values, fk_range)
    EFDs_given_fk_d(100, d, ft_values)  # Example slice for a known focal length of 100mm
    plt.show()

if __name__ == "__main__":
    main()
