import sqlite3
import math

def get_pnyt_list():   # Create a list of PNYT images
    """Gest list of ads numbers for PCs from database, for all animals"""
    pnyt_list = []
    limit: float = 19000
    
    con = sqlite3.connect('acc_animals.db')
    cur = con.cursor()

    with con as conn:
        cur = conn.cursor()
        cur.execute('SELECT ads, length(image_acc) FROM animals')
        rows = cur.fetchall()
        for row in rows:
            file_size = row[1]
            if math.isclose(file_size, limit, rel_tol=0.1, abs_tol=0.1):
                pnyt_list.append(row[0]) 

    return pnyt_list

# use
if __name__ == '__main__':  # This will run if the file is run directly
    pl = get_pnyt_list()
    print(pl)