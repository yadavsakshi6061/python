#Grayscale Images:
# Images with varying shades of gray, from black to white.

#Thresholded Images: 
# Grayscale images converted into binary form by setting a threshold, where pixels above the threshold are white and below are black.

#Indexed Images: 
# Grayscale images represented using a color lookup table, where each pixel value corresponds to an index in the table
# allowing for efficient storage of limited-color images.

#task2
import numpy as np
import pandas as pd

# Read binary data from file
with open('binary.bin', 'rb') as f: #read binary.
    binary_data = f.read()

# Convert binary data to a list of integers
binary_list = [int(byte) for byte in binary_data] 

# Convert the list into a NumPy array
binary_array = np.array(binary_list)

# Convert the NumPy array into a pandas DataFrame
df = pd.DataFrame(binary_array)

# Write DataFrame to CSV
df.to_csv('binary.csv', index=False, header=False) # index=False: This argument specifies that the index (row labels) of the DataFrame 
                                                   # header=False: This argument specifies that the header (column names)

# Print the contents of the CSV file
with open('binary.csv', 'r') as f:
    print(f.read())
