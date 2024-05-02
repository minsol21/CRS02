import numpy as np
from tqdm import tqdm
from simulate_fireflies import simulate_fireflies

def analyze_synchronization(N, L, r, T=5000, runs=50):
    amplitudes = []
    for _ in tqdm(range(runs), desc=f"Radius {r:.3f}"):
        flash_counts = simulate_fireflies(N, L, r, T)
        last_cycle_flashes = flash_counts[-L:]  # Last 50 time steps
        max_flashes = np.max(last_cycle_flashes)
        min_flashes = np.min(last_cycle_flashes)
        amplitude = (max_flashes - min_flashes)/2
        amplitudes.append(amplitude)
        average_amplitudes= np.mean(amplitudes)
    
    return average_amplitudes
