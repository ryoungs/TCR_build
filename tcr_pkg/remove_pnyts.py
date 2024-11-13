def remove_pnyts(category):   # remove PNYTs and return the number of images remaining
    if category == 'home':
        path = '../TCR/images/'
    elif category == 'foster':
        path = '../TCR/f_images/'  

    pnyt_list = []
    limit = 27500  # orbit and spearment came in at 26000... but still got in
    if int(limit) > 0:
        import os 
        for path, dirs, files in os.walk(path): 
            for f in files: 
                size=os.path.getsize(os.path.join( path, f))
                if size <= limit :   # No fix by changing to <= from <
                    # print(f + " " + str(size))
                    ads = f[:6]
                    # print(ads)
                    pnyt_list.append(ads)
                    # print(pnyt_list)
                    # os.remove(path+f) do I really need to do this? 
                    # If not removed thne the PNYT image remains in the database for that ads
                    # and it gets into Lightbox with the added Lightbox caption
                    # TBD ??  fix name and image caption spacing for PNYTs?
    return pnyt_list