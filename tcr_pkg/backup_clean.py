import os
import shutil
import datetime as dt
import tcr_pkg.delete_files_in_directory as df
#import delete_files_in_directory as df  # for testing

# backup database adding yesterday's date to backup file name
# TBD throws an error if dbase is not present!
def backup_clean():
    d0 = dt.date.today() - dt.timedelta(days=1)  # Yesterday's date
    dY = d0.isoformat()

    # Archive the database to TCR_archive folder
    src = './acc_animals.db'
    dest = './../TCR_archives/acc_animals_' + dY + '.db'

    if os.path.isfile(src):
        shutil.copy2(src, dest)
        os.remove(src)
    
    # Set path to remove images, thumbs, home, and foster pages 
    path = '../TCR/'
    
    if os.path.isfile(path+'index.html'):
        os.remove(path+'index.html')
        
    if os.path.isfile(path+'foster.html'):
        os.remove(path+'foster.html')
    
    # Remove files in build and target directories

    #df.delete_files_in_directory('./html/images/')     
    #df.delete_files_in_directory('./html/thumbs/')  

    df.delete_files_in_directory('../TCR/images/')     
    df.delete_files_in_directory('../TCR/thumbs/') 
    df.delete_files_in_directory('../TCR/f_images/')     
    df.delete_files_in_directory('../TCR/f_thumbs/') 
    df.delete_files_in_directory('../TCR/stats/')
    
    # use
if __name__ == '__main__':  # This will run if the file is run directly
    backup_clean()