import sqlite3

def put_animal_data(adata: list, database):
    """Insert All Animal Data from ACC Web into Sqlite Database - years, LOS, img_path to be created and added later"""
    try:
        db = sqlite3.connect(database)  # Connection
        cur = db.cursor()
    
        sq_insert_query=""" INSERT OR IGNORE INTO animals
        (ads,firstChoiceMessage,name,breed,species,age,initial_status,sex,altered,weight_lbs,arrival_date) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
    
        for item in adata:
            cur.execute(sq_insert_query,(item["ads"],item['firstChoiceMessage'],item['name'],item['breed'],item['species'],item['age'],item['initialStatus'],item['sex'],item['altered'],item['weight'],item['arrivalDate']))
            db.commit()
        print("Animal Database Updated with Raw Data")
        cur.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    
    finally:
        if db:
            db.close()
            #print("The SQLite connection is closed")
    

 
