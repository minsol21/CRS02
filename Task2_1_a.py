import numpy as np
import matplotlib.pyplot as plt
from count_neighbors import count_neighbors
from simulate_fireflies import simulate_fireflies


# Constants
N = 150           # Number of fireflies
L = 50            # Length of cycle
vicinity_radii = [0.05, 0.1, 0.5, 1.4]
simulation_steps = 5000


# Calculate the average number of neighbors for different r
positions = np.random.rand(N, 2)
cycles = np.random.randint(0, L, N)
average_neighbors = {r: np.mean(count_neighbors(positions, r)) for r in vicinity_radii}
print(f"the average number of neighbors per firefly:{average_neighbors}")

# Set up a figure for a 4x1 grid of plots
fig, axes = plt.subplots(4, 1, figsize=(10, 10), sharex=True)  # Share x-axis across subplots
colors = ['blue', 'green', 'red', 'purple']  # Define a list of colors for the plots

for i, r in enumerate(vicinity_radii):
    flash_counts = simulate_fireflies(N, L, r, simulation_steps)
    axes[i].plot(flash_counts, color=colors[i])
    axes[i].set_title(f'Radius {r}')
    axes[i].set_ylim(0, 150)  # Set vertical axis limit to [0, 150]
    axes[i].set_xlim(0, simulation_steps)  # Ensure x-axis shows all time steps
    if i == 3:
        axes[i].set_xlabel('Time Steps')
    axes[i].set_ylabel('Flashing Fireflies')

plt.suptitle('Number of Flashing Fireflies Over Time for Different Radii')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for the main title
plt.show()
