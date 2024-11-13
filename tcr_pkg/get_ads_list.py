import sqlite3

def get_ads_list():
    """Gest list of ads numbers from database, assumes all CATS"""
    ads_list = []
    try:
        con = sqlite3.connect('acc_animals.db')
        cur = con.cursor()
        # print("Connected to Animals")

        with con as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM animals')
            rows = cur.fetchall()
            for row in rows:
                ads_list.append(row[1])

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if con:
            con.commit()
            con.close()
            # print("The SQLite connection is closed")
            
    print("ADS list retreived from database")
    return ads_list


# use
if __name__ == '__main__':  # This will run if the file is run directly 
    adsList = get_ads_list()
    print(len(adsList))