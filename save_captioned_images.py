import io
import sqlite3
from PIL import Image, ImageDraw, ImageFont
import tcr_pkg.prep_image as preim
import tcr_pkg.get_ads_list as gal

def save_captioned_images(no_pub_list,ads_list,page):  # need to trap no image file error
    """Hard coded to adoptable and foster cats"""
            
    db = sqlite3.connect('acc_animals.db')
    cur = db.cursor()
    
    if page == 'home':
        querry = """SELECT * FROM animals WHERE ads = ? 
        AND species = 'CAT'
        AND firstChoiceMessage = 'ASK TO VISIT ME AT THE SHELTER'"""         
    elif page  == 'foster':
        querry = """SELECT * FROM animals WHERE ads = ? 
        AND species = 'CAT'       
        AND firstChoiceMessage = 'IN FOSTER CARE - ASK HOW TO MEET ME'"""
                
    for i, mmads in enumerate(ads_list):       
        cur.execute(querry, (mmads,))
        records = cur.fetchall()

        for item in records:
            if item[1] not in no_pub_list:
            #             if item[1] not in no_pub_list: - cat pc and pnyt lists to no_pub_list
                ads_img =  item[13]  #item[13] is the base image
                ads_name = item[3]
                ads_sex =  item[9]
                ads_age =  item[7]   # Age in years
                ads_status = item[8]
                
                if page == 'home':
                    f_name = '../TCR/images/' + mmads+ads_name + '.jpeg'   # Image Save Directory   
                elif page == 'foster':
                    f_name = '../TCR/f_images/' + mmads + ads_name + '.jpeg'   # Image Save Directory
                
                ads_sexage = ads_sex + ", " + format(ads_age, '.1f') + " Yrs, " + ads_status

                new_ads_img = Image.open(io.BytesIO(ads_img))
                    
                newimg = preim.prep_img(new_ads_img, ads_name, ads_sexage)
                
                newimg.save(f_name)

                cur.execute("""UPDATE animals SET img_path = ? WHERE ads = ?""",(f_name, mmads))
            
                db.commit()
    db.close()
    print('Captions added to base images')
    
if __name__ == '__main__':  # This will run if the file is run directly 
    ads_list = gal.get_ads_list()
    no_pub_list = []
    print(len(ads_list))
    save_captioned_images(no_pub_list,ads_list, 'home')  