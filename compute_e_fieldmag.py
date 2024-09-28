import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Load the CSV files for the x and y components of the electric field
E_x = pd.read_csv('xd.csv', header=None).values  # Assuming no header in CSV
E_y = pd.read_csv('yd.csv', header=None).values

# Compute the magnitude of the electric field at each point
E_magnitude = np.sqrt(E_x**2 + E_y**2)

# Find the maximum electric field magnitude and its location
max_magnitude = np.max(E_magnitude)
max_location = np.unravel_index(np.argmax(E_magnitude), E_magnitude.shape)

print(f'Maximum Electric Field Magnitude: {max_magnitude}')
print(f'Location of Maximum (row, column): {max_location}')


plt.imshow(E_magnitude, cmap='hot', interpolation='nearest') 
# color can be adjust, hot use really hot tone (make graph seem orange and red)
plt.colorbar(label='Electric Field Magnitude')
plt.title('Electric Field Magnitude Heat Map')
plt.show()
