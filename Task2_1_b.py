
import numpy as np
import matplotlib.pyplot as plt

def simulate_fireflies_extended_for_Task2_2(N, L, r, simulation_steps):
    positions = np.random.rand(N, 2)
    cycles = np.random.randint(0, L, N)
    flash_counts = []

    for step in range(simulation_steps):
        is_flashing = (cycles < L//2).astype(int)
        flash_counts.append(is_flashing.sum())

        distances = np.sqrt(((positions[:, np.newaxis, :] - positions[np.newaxis, :, :]) ** 2).sum(axis=2))
        neighbor_matrix = (distances < r) & (distances > 0)
        neighbors_flashing = np.dot(neighbor_matrix, is_flashing)

        for i in range(N):
            if neighbors_flashing[i] > neighbor_matrix[i].sum() / 2:
                cycles[i] = (cycles[i] + 1) % L

        cycles = (cycles + 1) % L

    return flash_counts[-L:]

def analysing_flash_amplitudes(N, L, r_range, simulation_steps, samples):
    radii = np.arange(r_range[0], r_range[1] + 0.025, 0.025)
    amplitude_averages = []

    for r in radii:
        amplitudes = []
        for _ in range(samples):
            last_L_flashes = simulate_fireflies_extended_for_Task2_2(N, L, r, simulation_steps)
            min_flashes = min(last_L_flashes)
            max_flashes = max(last_L_flashes)
            amplitude = (max_flashes - min_flashes) * 2
            amplitudes.append(amplitude)

        average_amplitude = np.mean(amplitudes)
        amplitude_averages.append(average_amplitude)

    return radii, amplitude_averages

def main():
    N = 150
    L = 50
    r_range = (0.025, 1.4)
    simulation_steps = 5000
    samples = 50

    radii, amplitude_averages = analysing_flash_amplitudes(N, L, r_range, simulation_steps, samples)

    plt.figure(figsize=(10, 6))
    plt.plot(radii, amplitude_averages, marker='o')
    plt.title('Average Amplitude of Flash Cycles vs. Vicinity Radius')
    plt.xlabel('Vicinity Radius')
    plt.ylabel('Average Amplitude of Flash Cycles')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
