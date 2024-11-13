import sqlite3

def get_LOS_by_sex_and_age(sex,age):
    locals_list = []    

    sqlstr = 'SELECT LOS FROM animals WHERE sex = ? and age = ?'

    try:
        con = sqlite3.connect('acc_animals.db')
        con.row_factory = lambda cursor, row: row[0]
    
        term = sex+age

        match term:
            case 'MK':
                print('Male Kitten')
                param = ('MALE',)
        
            case 'MA':
                print('Male Adult')
                param =  ('MALE',)

            case 'FK':
                print('Female Kitten')
                param = ('FEMALE',)

            case 'FA':
                print('Female Adult')
                param = ('FEMALE',)
            
            case _:
                print('No Case Considered')

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
    los_males = get_LOS_by_sex_and_age('F','A')
    print(los_males)