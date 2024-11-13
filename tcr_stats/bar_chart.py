import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the function to create the barplot
def barplot(category1, values1, category2, values2, labels, x_label='Categories', y_label='Values', title='Double Category Bar Plot'):
    # Combine the data from both categories into a pandas DataFrame
    data = pd.DataFrame({
        'Categories': labels * 2,  # Repeat the labels twice (once for each category)
        'Values': values1 + values2,  # Concatenate both value lists
        'Category': [category1] * len(values1) + [category2] * len(values2)  # Assign each value to its respective category
    })
    
    # Create the barplot using seaborn
    sns.barplot(x='Categories', y='Values', hue='Category', data=data)
    
    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    
    # Show the plot
    plt.show()

# Example usage
categories_labels = ['A', 'B', 'C', 'D']
category1_values = [10, 20, 15, 25]
category2_values = [12, 18, 22, 28]

barplot('Category 1', category1_values, 'Category 2', category2_values, categories_labels, x_label='Category', y_label='Value', title='Comparison Bar Plot')
