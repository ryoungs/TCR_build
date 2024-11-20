import sqlite3
import math
import pprint

def update_status(update_dict):   # Create a list of PNYT images
    """Update altered or PC status of name """
    
    con = sqlite3.connect('acc_animals.db')
    cur = con.cursor()
    
    for index, (key, value) in enumerate(update_dict.items()):
        param = (key,)
        if value == 'YES':
            query = """UPDATE animals SET altered = 'YES' WHERE name = ?"""
        elif value == 'PC':
            query = """UPDATE animals SET initial_status = 'GIVEN UP' WHERE name = ?"""
        
        cur.execute(query,param)
    con.commit()
    con.close()

# use
if __name__ == '__main__':  # This will run if the file is run directly
    update_dict={'DAHL':'PC','YASSO':'YES','LIBRARIAN':'YES',
                 'LONDON':'YES','NATHAN\'S FAMOUS':'YES',
                 'BIG PAWZ':'YES','MOLLY':'YES'}
    update_status(update_dict)

                  