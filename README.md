# CRS01 Exercise

## Team Members
- **Minsol Kim**
- **Bhargav Solanki**

## Overview
This repository hosts our group's submission for Task Sheet 2 of Collective robotics and scalability. The submission includes all necessary code, data visualizations (plots).

## Tasks
- **Task2.1a**: Calculate the average number of neighbors per firefly for vicinity distances r ∈ {0.05,0.1,0.5,1.4}
- **Task2.1b**: Determine the minimum and maximum number of concurrently flashing fireflies during the very last cycle (last L = 50 time steps starting from t = 4950)

## File structure and explaination
### Task2.1a
- count_neighbors.py and simulate_fireflies.py are used for the task2.1a in the file Task2_1_a.py
- plot1.png is the result of Task2_1_a.py
- The plot1.png shows the number of flashing fireflies over time for different radii. Each subplot represents a different radius at which fireflies interact with each other, and the graph tracks how the number of fireflies flashing synchronously changes over the course of 5000 time steps. 

**Analysis of Each Radius**

1. Radius 0.05 (Blue Line)
   - The blue line shows moderate fluctuations in the number of flashing fireflies, but the overall trend is fairly consistent without extreme peaks or troughs. This suggests that with a small radius, fireflies have fewer neighbors, resulting in less synchronization across the entire swarm.

2. Radius 0.1 (Green Line)
   - The green line demonstrates increased fluctuations compared to the smaller radius, which may indicate a better but still limited interaction among fireflies. The synchronization appears to improve slightly, possibly due to fireflies influencing more of their neighbors, but still does not achieve full synchronization.

3. Radius 0.5 (Red Line)
   - With the red line, there's a noticeable increase in the amplitude of fluctuations, and the pattern appears more chaotic. This suggests that a larger radius allows a firefly to influence and be influenced by more neighbors. The increased interactions can cause more dynamic changes in the state of flashing, leading to greater synchronization or desynchronization at different intervals.

4. Radius 1.4 (Purple Line)
   - The purple line shows very regular and high amplitude fluctuations, indicating strong synchronization across the swarm. At this radius, essentially every firefly is a neighbor of every other firefly due to the size of the radius relative to the square, allowing for very effective synchronization. The high consistency and amplitude in flashing suggest that most fireflies flash in unison or nearly so.

**General Observations**

- *Increasing Radius and Synchronization*: As the radius increases, the synchronization among fireflies tends to improve, with more fireflies flashing together. This is evident from the increase in the amplitude of fluctuations—larger radii tend to show more pronounced peaks and valleys, indicative of more fireflies flashing in unison.
- *Stability and Chaos*: Larger radii can also introduce more chaotic dynamics as fireflies are influenced by a larger number of neighbors. This can lead to rapid changes in the state of synchronization, which might explain the more chaotic appearance of the red graph.

**Conclusion**
From these observations, a larger radius generally leads to better synchronization among fireflies, as seen with the radius of 1.4, where the fluctuations are pronounced and regular, indicating strong collective behavior. However, the optimal radius for achieving synchronization without introducing too much chaos would need to balance these aspects, possibly favoring a slightly smaller radius than 1.4 to reduce the chaos while still maintaining good synchronization. Further analysis could involve looking at the specific dynamics at each radius to determine the best balance between radius size and synchronization efficiency.


### Task2.1b
- analyze_synchronization.py is used for the task2.1b in the file Task2_1_b_m.py
- plot2.png is the result of Task2_1_b_m.py

