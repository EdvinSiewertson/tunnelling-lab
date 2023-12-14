import numpy as np
import matplotlib.pyplot as plt
import os  # Import the os module for path manipulation

def plot_data(file_path, sample):
    x = []
    y = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Assuming the header is present, you can skip the first line
    for line in lines[1:]:
        # Assuming space-separated values, you can change the delimiter if needed
        values = line.strip().split()
        x.append(float(values[0]))  # Assuming the first column contains x values
        y.append(float(values[1]))  # Assuming the second column contains y values
    
    sorted_data = sorted(zip(x, y))
    x, y = zip(*sorted_data)

    return {
        'x': x,
        'y': y,
        'sample': sample,
    }

def plot_and_show(file_path, mark_peak=True):
    # Extract the sample name from the file path without the extension
    sample_name_with_extension = os.path.splitext(os.path.basename(file_path))[0]
    sample_name = sample_name_with_extension.split('_')[0]  # Extract only the part before the underscore
    
    data = plot_data(file_path, sample_name)

    if not data['x'] or not data['y']:
        print("No data points.")
        return

    plt.figure(figsize=(8, 6))
    plt.plot(data['x'], data['y'], '-o', label='Original Data')

    # Interactive region selection
    interval = plt.ginput(2, timeout=0)

    # Filter data within the selected interval
    interval_mask = (np.array(data['x']) >= min(interval[0][0], interval[1][0])) & (np.array(data['x']) <= max(interval[0][0], interval[1][0]))
    interval_x = np.array(data['x'])[interval_mask]
    interval_y = np.array(data['y'])[interval_mask]

    if len(interval_x) > 0:
        # Find the highest point in the interval
        max_index = np.argmax(interval_y)
        max_x = interval_x[max_index]
        max_y = interval_y[max_index]

        if mark_peak:
            # Mark the highest point in the interval
            plt.plot(max_x, max_y, 'ro', label='Highest Point of Peak')

            # Annotate the peak coordinates
            plt.text(max_x, max_y, f'Peak: ({max_x:.3f}, {max_y:.3f})', ha='right', va='bottom')

        plt.xlabel('Voltage (V)', fontsize=14)
        plt.ylabel('Current (A)', fontsize=14)
        plt.title(f'Voltage vs. Current for Sample {data["sample"]}', fontsize=14)
        plt.legend()

        # Display the plot
        plt.show()

        # Return relevant information
        return {
            'max_x': max_x,
            'max_y': max_y,
            'interval_x': interval_x,
            'interval_y': interval_y,
        }
    else:
        print("No data points in the selected interval.")
        return None

# Data files
files = ['Data/A5_2.txt', 'Data/B4_2.txt', 'Data/C1.txt', 'Data/D3.txt']

for file_path in files:
    mark_peak = file_path in ['Data/A5_2.txt', 'Data/B4_2.txt']
    result = plot_and_show(file_path, mark_peak)

    # Print additional information if the result is not None
    if result:
        print("Additional information:")
        print(f"Highest point of the peak: ({result['max_x']}, {result['max_y']})")
        print(f"Interval X values: {result['interval_x']}")
        print(f"Interval Y values: {result['interval_y']}")
