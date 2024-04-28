import numpy as np

def count_neighbors(positions, r):
    """Count neighbors for each firefly within a radius r."""
    distances = np.sqrt(((positions[:, np.newaxis, :] - positions[np.newaxis, :, :]) ** 2).sum(axis=2))
    neighbor_matrix = (distances < r) & (distances > 0)  # Exclude self in neighbor count
    neighbor_counts=neighbor_matrix.sum(axis=1)
    
    return neighbor_counts