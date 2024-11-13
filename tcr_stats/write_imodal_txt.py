from datetime import datetime, date      

def write_imodal_txt(im_path, txt_path):
    """write imodal.txt file in txt_path using images in im_path"""
    d0 = date.today().isoformat()
    
    path = im_path   # Location of the statistical images ready for web page display
    # txt_path - Location of text section to be included in index.html for modal img files
    
    # Input image file names:
    los_file = path + 'Cat_LOS_' + d0 +'.png'                  # LOS Histogram
    age_file = path + 'Cat_Ages_' + d0 +'.png'                 # Age Histogram
    status_file = path + 'cat_dog_status_count_'+ d0 + '.png'  # Cat & Dog Table
    category_file = path + 'System_' + d0 + '.png'        # System Category Pie Chart

    # constants
    tab1 = '    '
    tab2 = '        '
    NL    = '\n'
    altEq = ' alt = '

    fname =  txt_path + 'imodal.txt'          # text file section to be included in index.html
    f = open(fname,"w", encoding = "utf-8")   # open data file for text ouput

    # Cat LOS, Male/Female LOS plot image
    l0 = tab1+'<img class =' + '\"' + 'myImages' + '\"' + NL
    l1 = tab2+'id='+'\"' + 'myImg' + '\"' + ' src=' +'\"' + los_file + '\"' + NL
    l2 = tab2+ altEq + '\"' + 'LOS' + '\"' + ' width=' '\"'+ '50' + '\"' + 'height=' + '\"' + '50' + '\"' + '>'

    html_str_los = '<center>' + NL + l0 + l1 + l2
    print(html_str_los,file=f)

    # Cat, Male/Female Age plot image
    a0 = tab1+'<img class =' + '\"' + 'myImages'  + '\"' + NL
    a1 = tab2+'id='+'\"' + 'myImg' + '\"' + ' src=' +'\"' + age_file + '\"' + NL
    a2 = tab2+altEq + '\"' + 'Age' + '\"' + ' width=' '\"'+ '50' + '\"' + 'height=' + '\"' + '50' + '\"' + '>'

    html_str_age = a0+a1+a2
    print(html_str_age,file= f)

    # Cat & Dog status count table image
    a0 = tab1+'<img class =' + '\"' + 'myImages'  + '\"' + NL
    a1 = tab2+'id='+'\"' + 'myImg' + '\"' + ' src=' +'\"' + status_file + '\"' + NL
    a2 = tab2+altEq + '\"' + 'Status' + '\"' + ' width=' '\"'+ '50' + '\"' + 'height=' + '\"' + '50' + '\"' + '>'

    html_str_status = a0+a1+a2
    print(html_str_status,file= f)

    # All animals by category pie chart
    a0 = tab1+'<img class =' + '\"' + 'myImages'  + '\"' + NL
    a1 = tab2+'id='+'\"' + 'myImg' + '\"' + ' src=' +'\"' + category_file + '\"' + NL
    a2 = tab2+altEq + '\"' + 'Category' + '\"' + ' width=' '\"'+ '50' + '\"' + 'height=' + '\"' + '50' + '\"' + '>'

    html_str_category =  a0+a1+a2 + NL + '</center>'
    print(html_str_category,file= f)
    f.close() 

if __name__ == '__main__':  # This will run if the file is run directly  
    im_path = 'stats/'
    txt_path = 'html/html_inputs/'
    write_imodal_txt(im_path, txt_path)
        