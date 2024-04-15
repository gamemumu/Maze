import time
import csv

# def time_function(func, *args, **kwargs):
#     start_time = time.perf_counter()
#     result = func(*args, **kwargs)
#     end_time = time.perf_counter()
#     return end_time - start_time, result

# def write_timing_to_csv(graph_type, maze_size, wall_density, update_wall_times, neighbours_times, filename='timing_data.csv'):
#     with open(filename, mode='a', newline='') as file:
#         writer = csv.writer(file)
#         # Only write header if file is new
#         if file.tell() == 0:
#             writer.writerow(['Graph Type', 'Maze Size', 'Wall Density', 'Function', 'Average Time'])
        
#         avg_update_wall_time = sum(update_wall_times) / len(update_wall_times) if update_wall_times else 0
#         avg_neighbours_time = sum(neighbours_times) / len(neighbours_times) if neighbours_times else 0
        
#         writer.writerow([graph_type, maze_size, wall_density, 'updateWall', avg_update_wall_time])
#         writer.writerow([graph_type, maze_size, wall_density, 'neighbours', avg_neighbours_time])

def time_function(func, *args, repeats=100, **kwargs):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    average_time = sum(times) / len(times)
    
    return average_time, result

def write_timing_to_csv(graph_type, maze_size, update_wall_time, neighbours_time, filename='timing_data.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Only write header if file is new
        if file.tell() == 0:
            writer.writerow(['Graph Type', 'Maze Size', 'Function', 'Average Time'])
        
        # Write data to CSV
        writer.writerow([graph_type, maze_size, 'updateWall', update_wall_time])
        writer.writerow([graph_type, maze_size, 'neighbours', neighbours_time])