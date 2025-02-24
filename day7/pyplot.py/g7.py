# HORIZONTAL BAR PLOT
# Problem Statement: Displaying categorical data with long labels in a horizontal format.
# Question: Which category has the highest value in the horizontal bar chart?

# Create horizontal bar chart
import matplotlib.pyplot as plt
import numpy as np
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.barh(categories, values, color='orange')
plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Chart")
plt.show()