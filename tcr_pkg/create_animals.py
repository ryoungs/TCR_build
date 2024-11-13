import sqlite3

def  create_animals(database: str):               
    """ Creates DB and 'animals' Table if none exists"""
    db = sqlite3.connect(database)
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS animals(
        id integer PRIMARY KEY,
        ads text NOT NULL,
        firstChoiceMessage text,
        name text,
        breed text,
        species text,
        age text,
        years float,
        initial_status text,
        sex text,
        altered text,
        weight_lbs real,
        arrival_date numeric,
        image_acc blob,
        LOS integer,
        los_age text,
        img_path text);
        """)
    db.commit()
    
    db.close()

    # Example Use

if __name__ == '__main__':  # This will run if the file is run directly  
    db = 'acc_animals.db'
    create_animals(db)
    print("Animals Table Created in ", db)