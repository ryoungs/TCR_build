import os, sys
from datetime import datetime, date

# The path to the folder containing the tcr_pkg modules
PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep

# Put the rest of the modules on the path
sys.path.append(PATH)

import tcr_pkg.constants as K
import tcr_pkg.backup_clean as buc
import tcr_pkg.create_animals as ca
import tcr_pkg.get_all_acc_data as gacc
import tcr_pkg.put_animal_data as pa
import tcr_pkg.get_ads_list as gal 
import tcr_pkg.get_pc_list as gpc
import tcr_pkg.get_pnyt_list as gpn
import tcr_pkg.add_years as ayr 
import tcr_pkg.add_LOS as alos
import tcr_pkg.add_los_age as alosa
import tcr_pkg.get_base_image as gbi
import tcr_pkg.replace_spaces as rs
import tcr_pkg.get_ads_list as gal 
import tcr_pkg.save_captioned_images as psci
import tcr_pkg.create_thumbnails as ctns
import tcr_pkg.write_gallery_entry as wge
import tcr_pkg.cat_html_files as cat
import tcr_stats.list_age_by_sex as las
import tcr_stats.plot_hist_kde as phk
import tcr_stats.list_LOS_by_category as llos
import tcr_stats.count_all as call
import tcr_stats.plot_cat_dog_table as cdtbl
import tcr_stats.stacked_category_bar as sbar
import tcr_stats.write_imodal_txt as wim

# ----------------Backup and re-initialize animals database --------------#
# Backup & Clean Up +
buc.backup_clean()
print('Database backed up, Build and Target image directories cleaned')

# --------------Create a new database and table -------------------------#
dbase = 'acc_animals.db'  # sqlite3 database, table == animals
ca.create_animals(dbase)

acc_data = gacc.get_all_acc_data()

pa.put_animal_data(acc_data,dbase)
print('Raw data inserted into ',dbase) 

ads_list = gal.get_ads_list()  # ads list to update fields

ayr.add_years(ads_list)  # update years field
alos.add_LOS(ads_list)   # update LOS field
alosa.add_los_age(ads_list) # update young/adult field

url_img = K.URL_IMAGE
gbi.get_base_img(ads_list,url_img)

#  Pause for manual updates to database
input("Press ENTER to continue...")

# List the PCs and Picture Not Yet Taken (PNYTs) and concatenate for exclusion
pc_list = gpc.get_pc_list();
pnyt_list = gpn.get_pnyt_list()
no_pub_list = pc_list + pnyt_list  # List of animals to exclude from processing and display

""" TBD for html validation - need to remove spaces in displayed image file names
rs.replace_spaces('../TCR/thumbs/')   # Change spaces in image files to underline (html validation)
rs.replace_spaces('../TCR/images/') 
rs.replace_spaces('../TCR/f_images/') 
rs.replace_spaces('../TCR/f_thumbs/') 
"""

#--------------------- Create images with captions for Lightbox & write html template

psci.save_captioned_images(no_pub_list,ads_list, 'home')          # adds under and over captions to base image
psci.save_captioned_images(no_pub_list,ads_list,'foster')

ctns.create_thumbnails('../TCR/images/','../TCR/thumbs/',(150,150)) 
ctns.create_thumbnails('../TCR/f_images/','../TCR/f_thumbs/',(150,150)) 

wge.write_gallery_entry(no_pub_list,ads_list,'home')   # writes lightbox gallery of images w/ addt'l animal data
wge.write_gallery_entry(no_pub_list,ads_list,'foster')   # writes lightbox gallery of images w/ addt'l animal data

# Create some statistical plots and write modal html template for them

path = '../TCR/stats/'  #  Web Page stats image Path; destination for image files
d0 = date.today().isoformat()

# Get stats and write imodal
#  I ------------------ Plot Historgram of Cat Age & LOS by sex ---------------
type = 'AGE'
list1 = las.list_age_by_sex('M')
list2 = las.list_age_by_sex('F')
phk.plot_hist_kde(type,path,list1, list2, label1="Male Ages", label2="Female Ages", bins=5, xlabel="Age (years)", ylabel="Density")

type = 'LOS'
list1 =  llos.list_LOS_by_category('CAT','M')
list2 =  llos.list_LOS_by_category('CAT','F')
phk.plot_hist_kde(type,path, list1, list2, label1="Male LOS", label2="Female LOS", bins=5, xlabel="LOS (Days)", ylabel="Density")

# II ---------------- Create Side by Side table of Cat and Dog Totals ---------

fname = path + 'cat_dog_status_count_' + d0 + '.png'

# create_fill_all_data()
cat_total = call.count_all('CAT',path)
dog_total = call.count_all('DOG',path)

cdtbl.plot_cat_dog_table(fname, cat_total, dog_total)

# III ---------------- Create Stacked Bar Chart for Cat, Dog, All Animals Totals ---------
sbar.stacked_category_bar(path)

#  Create text file for modal plots on home page
# Writes an html file (tag) with the stat images 

im_path = 'stats/'
txt_path = 'html/html_inputs/'
wim.write_imodal_txt(im_path, txt_path)

# Finally, concatenate the html template sections into home and foster page files

cat.cat_html_files('home')                  # creates index.html and foster.html
cat.cat_html_files('foster')       
