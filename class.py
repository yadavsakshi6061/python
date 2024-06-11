import numpy as np
import pandas as pd 

# Reading a text file
#with open('para.txt', 'r') as f:
    #data = f.read()

#print(data)

# Writing to a text file
with open('para.txt', 'w') as f:
    f.write('wlcm ')

#2 displays the img file 
import matplotlib.pyplot as plt  # Importing matplotlib for plotting
from PIL import Image  # Importing Image module from Pillow package (PIL)
# Note: if PIL is not installed, install it using 'pip install Pillow'

img = Image.open('sign.jpg')  # Open the image file named 'sign.jpg'

# Display some information about the image
print(img)  # Print the image object
print(img.format)  # Print the format of the image (e.g JPEG, PNG, etc.)
print(img.size)  # Print the dimensions of the image (width, height)
print(img.mode)  # Print the mode of the image (e.g., RGB, grayscale)

# Display the image using matplotlib
plt.imshow(img)  # Plot the image
plt.axis('off')  # Turn off axis labels
plt.show()  # Show the plot

#3 reads data from an Excel file ('file.xlsx') using pandas 

import numpy  as np 
import pandas as pd 

df =pd.read_excel('file.xlsx') 
print(df)

#4 Read the CSV file into a pandas DataFrame

df = pd.read_csv("customer.csv")
print(df)


