import sys 
import sqlite3
#import get_ads_list as gal

def add_los_age(ads_list):
    db = sqlite3.connect('acc_animals.db')
    cur = db.cursor()
    
    for i, mmads in enumerate(ads_list):
        cur.execute('SELECT * FROM animals WHERE ads = ?', (mmads,))
        records = cur.fetchall()    
        for item in records:
            years =  item[7]         # grab age in years  (numeric)
            ads = item[1]
            if years <= 0.41:
                los_age = 'young'
            else:
                los_age = 'adult'

            cur.execute("""UPDATE animals SET los_age = ? WHERE ads = ?""",(los_age, mmads))
            db.commit()
    print("los_age field updated")
    db.close()
 
# use
if __name__ == '__main__':  # This will run if the file is run directly
    ads_list = gal.get_ads_list()
    add_los_age(ads_list)