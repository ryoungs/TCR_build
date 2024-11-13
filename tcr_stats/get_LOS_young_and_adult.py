import sqlite_utils

def list_los_by_gender_and_age(database_path, table_name):
    # Connect to the database
    db = sqlite_utils.Database(database_path)
    
    # SQL query to get LOS data by gender and age group
    query = f"""
    SELECT 
        gender,
        CASE 
            WHEN length_of_stay <= 0.5 THEN 'Less than or equal to 0.5 years'
            ELSE 'Greater than 0.5 years'
        END as age_group,
        COUNT(*) as count
    FROM {table_name}
    WHERE gender IN ('male', 'female')
    GROUP BY gender, age_group;
    """
    
    # Execute the query and fetch the results
    result = db.query(query)
    
    # Print the results
    print("Length of Stay (LOS) by Gender and Age Group:")
    for row in result:
        print(f"Gender: {row['gender']}, Age Group: {row['age_group']}, Count: {row['count']}")

# Example usage

if __name__ == '__main__':  # This will run if the file is run directly  
	database_path = 'acc_animals.db'
	table_name = 'animals'
	list_los_by_gender_and_age(database_path, table_name)

