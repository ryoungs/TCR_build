import sqlite3
from datetime import datetime, date
from sqlite_utils import Database

def count_all(type,path):
    """ Count Males, Females, Altered, Status"""
    if type == 'CAT':
        species = 'CAT'
    elif type == 'DOG':
        species = 'DOG'
        
    d0 = date.today().isoformat()
    fn_status = path + species + '_status_count_' + d0 + '.txt'  
    fn = open(fn_status,"w", encoding = "utf-8")   #Open data file for text ouput

    db = Database('acc_animals.db')
    
    countm =  db["animals"].count_where("sex = ? AND species = ?", ['MALE',type,])
    countf =  db["animals"].count_where("sex = ? AND species = ?", ['FEMALE',type,])
    counta =  db["animals"].count_where("altered = ? AND species = ?", ['YES',type,])
    counts =  db["animals"].count_where("initial_status = ? AND species = ?", ['STRAY',type,])
    countg =  db["animals"].count_where("initial_status = ? AND species = ?", ['GIVEN UP',type,])
    countt =  db["animals"].count_where("species = ?", [type,])
    countua = countt-(counts + countg)
    
    m = [countm, countf,counta,counts, countg, countua, countt] 

    tbl = ("Count of All " + type + "s_" + d0 + "\n" + 
            "Males:      "+ str(m[0]) + "\n" +  
            "Females:    "+ str(m[1]) + "\n" +
            "Altered:    "+ str(m[2]) + "\n" +
            "Strays:     "+ str(m[3]) + "\n" +
            "Given UP:   "+ str(m[4]) + "\n" +
            "Unassigned: "+ str(m[5]) + "\n" +
            "Total:      "+ str(m[6])
            )
        
    # print(tbl,file=fn)
    fn.close()
    # print("Count_All " + type + "S Completed")
    
    return m

# Use
if __name__ == '__main__':  # This will run if the file is run directly  
    path = 'html/plots/'
    count_all('DOG',path) 
