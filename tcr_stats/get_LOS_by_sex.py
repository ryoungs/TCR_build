import sqlite3

def get_LOS_by_sex(sex):
    locals_list = []    
    sqlstr = 'SELECT LOS FROM animals WHERE sex = ?'

    try:
        con = sqlite3.connect('acc_animals.db')
        con.row_factory = lambda cursor, row: row[0]
    
        if sex == 'M':
            param = ('MALE',)
        else:
            param = ('FEMALE',)
            
        print("Connected to Animals")

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
            print("The SQLite connection is closed")
            
    return rows

#  Example - requires access to acc_animals.db 
if __name__ == '__main__':  # This will run if the file is run directly  
    los_males = get_LOS_by_sex('M')
    print(los_males)