import numpy as np        # Import numpy for numerical calculations
import pandas as pd       # Import pandas for data manipulation

# Step 1: Load the data from the Excel file
data = pd.read_excel('scan_output_A.xlsx', header=None)  # Load data without header

# Step 2: Convert the data to a NumPy array
data_array = data.values # Convert DataFrame to NumPy array


delta_v_x = -(np.diff(data_array, axis =1)) # axis= 1 mean operation along the row
delta_v_x = delta_v_x[0:-1,:]
# Step 4: Create a DataFrame from the delta_v_x array
delta_v_x_df = pd.DataFrame(delta_v_x)

# Step 5: Save the DataFrame to a CSV file
# Replace 'delta_v_x_output.csv' with your desired output file name
delta_v_x_df.to_csv('x.csv', index=False, header=False)

print(delta_v_x.shape)

