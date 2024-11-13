import sqlite3

def delete_pc(ads_list, NPC):
    db = sqlite3.connect('acc_animals.db')
    cur = db.cursor()
    
    if NPC > 0:
        for i, mmads in enumerate(ads_list):

            cur.execute('SELECT * FROM animals WHERE ads = ?', (mmads,))
            records = cur.fetchall()
            
            for item in records:
                pc =  str(item[8])         # grab initial_status field
                id = item[0]
                if pc == 'PROTECTIVE CUSTODY':          # Check for PC text in field
                    cur.execute('DELETE FROM animals WHERE id=?', (id,))      
                    db.commit()
    db.close()
    print(str(NPC) + " PC animals deleted from database")