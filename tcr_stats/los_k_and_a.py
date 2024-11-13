import sqlite3
import statistics as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def select_animals_by_sex_and_age(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # SQL query for years <= 0.45
    query_less_equal_4_5 = """
    SELECT LOS FROM animals
    WHERE (sex = 'FEMALE' OR sex = 'MALE') AND years <= 0.35
    """
    cursor.execute(query_less_equal_4_5)
    # Fetch all results where years <= 4.5
    years_less_equal_4_5 = cursor.fetchall()
    
    # SQL query for years > 4.5
    query_greater_4_5 = """
    SELECT LOS FROM animals
    WHERE (sex = 'FEMALE' OR sex = 'MALE') AND years > 0.35
    """
    cursor.execute(query_greater_4_5)
    # Fetch all results where years > 4.5
    years_greater_4_5 = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return both lists
    return years_less_equal_4_5, years_greater_4_5

# Define the function to create the barplot
def barplot(categories, values, x_label='Categories', y_label='Values', title='Simple Bar Plot'):
    # Combine the categories and values into a pandas DataFrame
    data = pd.DataFrame({'Categories': categories, 'Values': values})
    
    # Create the barplot using seaborn
    sns.barplot(x='Categories', y='Values', data=data)
    
    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    
    # Show the plot
    plt.show()

# Example usage
db_path = 'acc_animals.db'
age_less_equal_4_5, age_greater_4_5 = select_animals_by_sex_and_age(db_path)

adult = st.mean(x[0] for x in age_greater_4_5)
adultsd = st.stdev(x[0] for x in age_greater_4_5)

kitten = st.mean(x[0] for x in age_less_equal_4_5)
kittensd = st.stdev(x[0] for x in age_less_equal_4_5)

categories = ['Kitten', 'Adult']
values =[kitten, adult]

barplot(categories, values, x_label='Category', y_label='Value', title='Comparison of Two Categories')

