import sqlite3

def get_LOS():
    locals_list = []    
    sqlstr = 'SELECT LOS FROM animals WHERE species = ?'

    try:
        con = sqlite3.connect('acc_animals.db')
        con.row_factory = lambda cursor, row: row[0]

        param = ('CAT',)
            
        with con as conn:
            cur = conn.cursor()
            cur.execute(sqlstr,param)
            rows = cur.fetchall()           

    except sqlite3.Error as error:
        print("Failed to count LOS", error)
    finally:
        if con:
            con.commit()
            con.close()
            
    return rows

# use
if __name__ == '__main__':  # This will run if the file is run directly 
    klos = get_LOS()
    print(klos)
