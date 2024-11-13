import sqlite3

def list_age_by_sex(sex) -> list[float]:
    """Gest list of male or female ages from database"""
    age_list = []    
    try:
        con = sqlite3.connect('acc_animals.db')
        con.row_factory = lambda cursor, row: row[0]
    
        if sex == 'M':
            param = ('MALE',)
            sqlstr = 'SELECT years FROM animals WHERE sex = ?'
        else:
            param = ('FEMALE',)
            sqlstr = 'SELECT years  FROM animals WHERE sex = ?'

        with con as conn:
            cur = conn.cursor()
            cur.execute(sqlstr,param)
            rows = cur.fetchall()           

    except sqlite3.Error as error:
        print("Failed to count ages", error)
    finally:
        if con:
            con.commit()
            con.close()
            
    return rows

# Use
if __name__ == '__main__':  # This will run if the file is run directly  
    mages = list_age_by_sex('M')
    for age in mages:
        print(f"{age:.2f}")
