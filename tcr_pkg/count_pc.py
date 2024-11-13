import sqlite3

def count_pc():
    db = sqlite3.connect('acc_animals.db')
    cur = db.cursor()
    
    param = ('PROTECTIVE CUSTODY',)
    
    cur.execute('SELECT COUNT(id) FROM animals WHERE initial_status =?',param) 
    count = cur.fetchone()[0]
    
    db.commit()
    db.close()
    
    return count