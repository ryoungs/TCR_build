import sqlite3
import requests

def get_base_img(ads_list, url_img):
    """ Get base image for ADS Numberss """
    db = sqlite3.connect('acc_animals.db')
    cur = db.cursor()

# Note - i needed here or I get a INSERT tuple error 
# Note - Pylance does throw an error here for having i in for statement witout i in body
#        but no error is thrown in archive/test_get_put_image0.py
    for i, mmads in enumerate(ads_list):
        
        im = requests.get(url_img + mmads + ".jpeg", timeout=20)
        img = im.content
        
        im_bin = sqlite3.Binary(im.content)
        cur.execute("""UPDATE animals SET image_acc = ? WHERE ads = ?""",(im_bin, mmads))

    db.commit()
    db.close()
    print("Base images retreived from AACACC Website")