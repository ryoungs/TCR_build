
import sqlite3
import datetime

def add_years(ads_list):
    """Extract years from age (string) field and add to years (integer) field"""
    # TBD - add an integer months column and treat ADULT differently (how?)
    db = sqlite3.connect('acc_animals.db')
    cur = db.cursor()
    
    for i, mmads in enumerate(ads_list):

        cur.execute('SELECT * FROM animals WHERE ads = ?', (mmads,))
        records = cur.fetchall()
        
        for item in records:
            dt =  str(item[6])         # grab age text field
            if dt == 'ADULT':          # Check for 'ADULT' text in field
                years = 1.0            # Assume age is 1 yr for ADULT
            elif dt == 'UNKNOWN' or dt == 'None':  # May need to catch other omissions in future
                years = 0.0
            elif dt == 'JUVENILE':
                years = 0.5
            else:
                n=dt.split('y')[0]    # split out the number of years
                d =dt.split('m')[0]   # split out yeas & months
                dd = d.split(',')[1]  # split out months from [years & months]
                nn=float(n)           # convert years from str to float
                ddd=float(dd)         # convert months from str to float
                years=nn+(ddd/12)     # compute age in years + decimal months
                
            cur.execute("""UPDATE animals SET years = ? WHERE ads = ?""",(years, mmads))

    db.commit()
    db.close()
    print("Years field updated")
    
    #use 
    if __name__ == '__main__':  # This will run if the file is run directly 
        adsList = gal.get_ads_list()
        print(len(adsList))
        add_years(adsList)