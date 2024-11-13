import sqlite3
import statistics as st

def list_LOS_by_category(species,param) -> list[int]:
    """
        creates a list of LOS by >> species, sex, young-adult, adop-foster 
        arguments param:
        species         == 'DOG' or 'CAT'  
        sex             == 'M' or 'F'  and other categories (Young/Adult and Adopt/Foster)
        young/adult     == 'Young' or 'Adult' 
        adopt/foster    == 'Adopt' or 'Foster' 
    """  

    try:
        con = sqlite3.connect('acc_animals.db')
        con.row_factory = lambda cursor, row: row[0]
    
        if species == 'CAT' and param == 'M':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'CAT' and sex =='MALE'"""
        elif species == 'CAT' and param == 'F':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'CAT' and sex =='FEMALE'"""   
        elif species == 'CAT' and param == 'Young':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'CAT' and los_age =='young'"""
        elif species == 'CAT' and param == 'Adult':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'CAT' and los_age =='adult'""" 
        elif species == 'CAT' and param == 'Adopt':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'CAT' and firstChoiceMessage =='ASK TO VISIT ME AT THE SHELTER'""" 
        elif species == 'CAT' and param == 'Foster':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'CAT' and firstChoiceMessage =='IN FOSTER CARE - ASK HOW TO MEET ME'"""   
        elif species == 'DOG' and param == 'M':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'DOG' and sex =='MALE'"""
        elif species == 'DOG' and param == 'F':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'DOG' and sex =='FEMALE'"""   
        elif species == 'DOG' and param == 'Young':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'DOG' and los_age =='young'"""
        elif species == 'DOG' and param == 'Adult':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'DOG' and los_age =='adult'""" 
        elif species == 'DOG' and param == 'Adopt':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'DOG' and firstChoiceMessage =='ASK TO VISIT ME AT THE SHELTER'""" 
        elif species == 'DOG' and param == 'Foster':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'DOG' and firstChoiceMessage =='IN FOSTER CARE - ASK HOW TO MEET ME'""" 
        elif species == 'Both' and param == 'Both':
            sqlstr = """SELECT LOS FROM animals WHERE species = 'DOG' or species =='CAT'"""

        with con as conn:
            cur = conn.cursor()
            cur.execute(sqlstr)
            rows = cur.fetchall()           

    except sqlite3.Error as error:
        print("Failed to count LOS", error)
    finally:
        if con:
            con.commit()
            con.close()

    return rows

if __name__ == '__main__':  # This will run if the file is run directly  
    # mlos = list_LOS_by_category('CAT','Foster')
    #for los in mlos:
        #print(los)   
    """    
        print(st.median(list_LOS_by_category('CAT','M')))
        print(st.median(list_LOS_by_category('CAT','F')))
        print(st.median(list_LOS_by_category('CAT','Young')))
        print(st.median(list_LOS_by_category('CAT','Adult')))
        print(st.median(list_LOS_by_category('CAT','Adopt')))
        print(st.median(list_LOS_by_category('CAT','Foster'))) 
    """  
    cat_los =[st.median(list_LOS_by_category('CAT','M')),
              st.median(list_LOS_by_category('CAT','F')),
              st.median(list_LOS_by_category('CAT','Young')),
              st.median(list_LOS_by_category('CAT','Adult')),
              st.median(list_LOS_by_category('CAT','Adopt')),
              st.median(list_LOS_by_category('CAT','Foster'))]
    
    print(cat_los)
    
    if len(list_LOS_by_category('DOG','Young')) == 0:   # Often an empty list on daily basis
        young_dog_med = 0
    else:
        young_dog_med = st.median(list_LOS_by_category('DOG','Young'))
        
    dog_los =[st.median(list_LOS_by_category('DOG','M')),
            st.median(list_LOS_by_category('DOG','F')),
            young_dog_med,
            st.median(list_LOS_by_category('DOG','Adult')),
            st.median(list_LOS_by_category('DOG','Adopt')),
            st.median(list_LOS_by_category('DOG','Foster'))]
    
    print(dog_los)
    
    cats_dogs = st.median(list_LOS_by_category('Both','Both'))
    print(cats_dogs)