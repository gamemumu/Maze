import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('timing_data.csv')

# Group the data by Maze Size and Function
grouped = df.groupby(['Maze Size', 'Graph Type'])['Average Time'].mean().unstack()

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(grouped.index))
width = 0.2

ax.bar(x - width, grouped['updateWall']['ls'], width, label='ls')
ax.bar(x, grouped['neighbours']['ls'], width, label='ls')
ax.bar(x + width, grouped['updateWall']['mt'], width, label='mt')

ax.bar(x - width + 3, grouped['neighbours']['mt'], width, label='mt')
ax.bar(x + 3, grouped['updateWall']['ls'], width, label='ls')
ax.bar(x + width + 3, grouped['neighbours']['ls'], width, label='ls')

ax.bar(x - width + 6, grouped['updateWall']['mt'], width, label='mt')
ax.bar(x + 6, grouped['neighbours']['mt'], width, label='mt')
ax.bar(x + width + 6, grouped['updateWall']['ls'], width, label='ls')

ax.set_xticks(x + 3)
ax.set_xticklabels(['Small', 'Medium', 'Large'])
ax.set_xlabel('Maze Size')
ax.set_ylabel('Average Time (s)')
ax.set_title('Running times for Insert row/column vs Maze Size')
ax.legend()

plt.show()