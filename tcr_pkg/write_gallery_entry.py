import os
import sqlite3
import pathlib

def write_gallery_entry(no_pub_list,ads_list,category):
    """  TBD  this is putting pnyts on list when getting additional data for each animal"""
    # constants
    cont = '<div class = \"lbcontainer\">'
    dv   = '    <div class = \"gallery\">'
    ain  = '        <a href = '
    dL   = ' data-Lightbox = \"models\" '
    ith  = '<img src ='
    aout = '</a>'
    tab1 = '    '
    tab2 = '        '
    dvout = '</div>'
    NL    = '\n'
    altEq = ' alt = '

    db = sqlite3.connect('acc_animals.db')
    cur = db.cursor()

    if category == 'home':
        querry = """SELECT * FROM animals WHERE ads = ? 
        AND species = 'CAT'
        AND firstChoiceMessage = 'VISIT ME AT THE SHELTER'"""    
        # Animal data file as of today
        fname =  "html/html_inputs/lightbox_home_images.txt"        
        f = open(fname,"w", encoding = "utf-8")            # open data file for text ouput
        pimages = 'images/'
        pthumb = 'thumbs/'
    elif category == 'foster':
        querry = """SELECT * FROM animals WHERE ads = ? 
        AND species = 'CAT'       
        AND firstChoiceMessage = 'IN FOSTER CARE'"""
        fname =  "html/html_inputs/lightbox_foster_images.txt"        # Animal data file as of today
        f = open(fname,"w", encoding = "utf-8")            # open data file for text ouput
        pimages = 'f_images/'
        pthumb ="f_thumbs/"
        
    print(cont+NL+dv, file=f)

    for i, mmads in enumerate(ads_list):
        cur.execute(querry, (mmads,))
        records = cur.fetchall()
        
        for item in records:
            #if item[14] != "NULL":    # this was suposed to be set to NULL on input for pnyts  TBD
            if item[1] not in no_pub_list:
                ads_name =   item[3]
                ads_breed =  item[4]
                ads_age =    item[7]
                ads_status = item[8]
                ads_sex =    item[9]
                ads_altered =   item[10]
                ads_los =       item[14]
                ads_img_path =  item[16]  #item[11] is the captioned image path
                            
                p = pathlib.Path(ads_img_path)
                p1 = p.parts[1]
                #p2 = os.path.splitext(p.parts[2])[0]
                p2 = os.path.splitext(p.parts[3])[0]

                # img = '\"' + str(p1) + "/" + str(p2) + ".jpeg" + '\"'
                img = '\"' + pimages + str(p2) + '.jpeg' + '\"'

                imgT = '\"' + pthumb + str(p2) + "_T" + ".jpeg" + '\"'

                if ads_altered == 'YES':         # Altered or not
                    C1 = 'Altered, '
                else:
                    C1 = 'Not Altered, '

                C2 = ads_breed +', '  # Breed

                """if ads_status == 'STRAY':     # initial_status
                    C3 = 'Stray,'
                else: 
                    C3 = 'Give-up,'"""
                    
                C4 = ' In the Shelter for ' + str(ads_los) + ' Days'
                
                C5 = altEq + '\"' + ads_name + '\"'

                dT = 'data-title=' + '\"' + C1 + C2 + C4 + '\" ' + '>'

                html_str = ain + img + dL + NL + tab2 + dT + NL + tab2 + ith+imgT + C5 + '>' + NL + tab2 + aout

                print(html_str,file= f)
                
    print(tab1+dvout+NL+dvout,file=f)   

    f.close()
    
    # use
# if __name__ == '__main__':  # This will run if the file is run directly
