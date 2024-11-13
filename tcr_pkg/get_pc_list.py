import sqlite3

def get_pc_list():
    """Gest list of ads numbers for PCs from database, for all animals"""
    pc_list = []
    param = ('PROTECTIVE CUSTODY',)
     
    try:
        con = sqlite3.connect('acc_animals.db')
        cur = con.cursor()

        with con as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM animals WHERE initial_status =?',param)
            rows = cur.fetchall()
            for row in rows:
                pc_list.append(row[1])
                
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if con:
            con.commit()
            con.close()
            # print("The SQLite connection is closed")
            
    print("PC list retreived from database")
    return pc_list
    
# Use
if __name__ == '__main__':  # This will run if the file is run directly 
    pclist = get_pc_list()
    print(pclist)