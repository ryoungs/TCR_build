import sys 
import sqlite3
import datetime as dt
# import get_ads_list as gal

def add_LOS(ads_list):
    db = sqlite3.connect('acc_animals.db')
    cur = db.cursor()
        
    d0 = dt.date.today().isoformat()
    
    for i, mmads in enumerate(ads_list):
        cur.execute('SELECT * FROM animals WHERE ads = ?', (mmads,))
        records = cur.fetchall()    
        for item in records:
            arr_date =  item[12]         # grab arrival_date field  (numeric)
            ads = item[1]
            #cur.execute("""UPDATE animals SET years = ? WHERE ads = ?""",(years, mmads))
            ard1 = arr_date.split('-'[0])
            yr = int(ard1[0])
            if yr < 2024:
                yr = 2024
            mo = int(ard1[1])
            d =  int(ard1[2])
            arivaldate = dt.date(yr,mo,d) 

            td = dt.date.today()

            LOS = (td-arivaldate).days
            
            cur.execute("""UPDATE animals SET LOS = ? WHERE ads = ?""",(LOS, mmads))
            db.commit()
    print("LOS field updated")
    db.close()
 
# use
if __name__ == '__main__':  # This will run if the file is run directly
    ads_list = gal.get_ads_list()
    add_LOS(ads_list)
    