import numpy as np

def simulate_fireflies(N, L, r, simulation_steps):
    """Simulate the fireflies synchronization over time with specific radius r."""
    positions = np.random.rand(N, 2)
    cycles = np.random.randint(0, L, N)
    flash_counts = []

    for _ in range(simulation_steps):
        # Determine current state: 1 if flashing, 0 if not
        is_flashing = (cycles < L//2).astype(int)
        flash_counts.append(is_flashing.sum())

        # Calculate neighbors and check if the majority is flashing
        distances = np.sqrt(((positions[:, np.newaxis, :] - positions[np.newaxis, :, :]) ** 2).sum(axis=2))
        neighbor_matrix = (distances < r) & (distances > 0)
        neighbors_flashing = np.dot(neighbor_matrix, is_flashing)

        # Adjust cycle based on neighbors
        for i in range(N):
            if neighbors_flashing[i] > neighbor_matrix[i].sum() / 2:  # Majority is flashing
                cycles[i] = (cycles[i] + 1) % L  # Sync by shortening the flash phase

        # Update cycles
        cycles = (cycles + 1) % L

    return flash_counts
