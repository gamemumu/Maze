import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('timing_data.csv')
data['Average Time'] = pd.to_numeric(data['Average Time'], errors='coerce')  # Convert to float, coerce errors
data.dropna(subset=['Average Time'], inplace=True)  # Remove any rows that couldn't be converted to numbers

# Plotting
# Convert the 'Maze Size' to a categorical type with the specified order
size_order = ['5x5', '10x10', '50x50', '70x100']
data['Maze Size'] = pd.Categorical(data['Maze Size'], categories=size_order, ordered=True)

# Now we can plot the data with the sizes in the correct order
plt.figure(figsize=(10, 6))
for label, group_df in data.groupby('Graph Type'):
    group_df = group_df.groupby('Maze Size')['Average Time'].mean().reindex(size_order)
    plt.plot(group_df.index, group_df.values, label=label, marker='o')

plt.title('Performance Comparison')
plt.xlabel('Maze Size')
plt.ylabel('Average Time (seconds)')
plt.legend(title='Graph Type')
plt.show()