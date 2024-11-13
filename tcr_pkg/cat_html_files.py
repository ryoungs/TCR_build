def cat_html_files(category):

    if category == 'home':
        out_file_path = '../TCR/index.html'
        filenames = ['html/html_inputs/index1.txt',     #  index.html TOP section to Trigger the Modal  (constant)
                     'html/html_inputs/imodal.txt',     #  Trigger Modal to  Modal  - stat images (written each day)
                     'html/html_inputs/imodal2.txt',    #  Short section at end of stat image modals (constant)
                     'html/html_inputs/lightbox_home_images.txt',  # Long section of Lightbox2 images (written each day)
                     'html/html_inputs/index2.txt']     #  End of index.html
    elif category == 'foster':
        out_file_path = '../TCR/foster.html'
        filenames = ['html/html_inputs/f_index1.txt',
                     'html/html_inputs/lightbox_foster_images.txt', 
                     'html/html_inputs/f_index2.txt']
        
    with open(out_file_path, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
                    
# Use
if __name__ == '__main__':  # This will run if the file is run directly
    cat_html_files('home')
    cat_html_files('foster')