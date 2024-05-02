import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from simulate_fireflies import simulate_fireflies
from analyze_synchronization import analyze_synchronization

# Parameters
N = 150
L = 50
R = np.arange(0.025, 1.425+0.025, 0.025) #to include 1.425 at the end

# Collect data
average_amplitudes = []
for r in tqdm(R, desc="Overall Progress"):
    average_amplitudes.append(analyze_synchronization(N, L, r))

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(R, average_amplitudes, marker='o')
plt.xlabel('Vicinity radius (r)')
plt.ylabel('Average synchronization amplitude')
plt.title('Effect of Vicinity Radius on Synchronization Amplitude')
plt.grid(True)
plt.show()
