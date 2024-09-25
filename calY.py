import numpy as np        # Import numpy for numerical calculations
import pandas as pd       # Import pandas for data manipulation

# Step 1: Load the data from the Excel file
data = pd.read_excel('scan_output_A.xlsx', header=None)  # Load data without header

# Step 2: Convert the data to a NumPy array
data_array = data.values  # Convert DataFrame to NumPy array

# Step 3: Calculate differences for y components (column-wise difference)
delta_v_y = -(np.diff(data_array, axis=0))  # Differences in y (shape will be (19, 25))
delta_v_y = delta_v_y[:,0:-1]

# Step 4: Save the y differences to a CSV file
y_diff_df = pd.DataFrame(delta_v_y)  # Create DataFrame from the y differences
y_diff_df.to_csv('y.csv', index=False, header=False)  # Save as CSV without index and header

print(delta_v_y.shape)
print(data_array.shape)