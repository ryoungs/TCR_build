import matplotlib.pyplot as plt
from datetime import datetime, date
from sqlite_utils import Database
import seaborn as sns

def category_pie_chart(my_database, path):  # Pie chart with percentage inventory of animals of each category from ALL animals in shelter
    d0 = date.today().isoformat()
    fn_category = path + 'By_category_' + d0 + '.txt'  
    fs_category = path + 'By_category_' + d0 + '.png'       
    fn = open(fn_category,"w", encoding = "utf-8")   #Open data file for text ouput
    db = Database(my_database)
    print(fs_category)
        
    countA =  db["animals"].count_where("firstChoiceMessage = ?", ['ADOPTION PENDING',])
    countB =  db["animals"].count_where("firstChoiceMessage = ?", ['ADOPTION PENDING (OFFSITE)',])
    countC =  db["animals"].count_where("firstChoiceMessage = ?", ['ASK TO VISIT ME AT THE SHELTER',])
    countD =  db["animals"].count_where("firstChoiceMessage = ?", ['IN FOSTER CARE - ASK HOW TO MEET ME',])
    countE =  db["animals"].count_where("firstChoiceMessage = ?", ['',])
    countF =  db["animals"].count
    
    # n    = [countA, countB, countC, countD, countE, countF]   
      
    plt_data =  [countA, countB, countC, countD, countE]      
    keys = [ 'Pending\n Adopt ','Offsite Adopt   \n(Foster to Adopt)','In Shelter','In Foster','Rescue\nReclaim']   
    """
    tbl = ("Category Count "    + d0        + "\n" + 
           "Pending Adopt:    " + str(n[0]) + "\n" +  
           "Offsite Adopt:    " + str(n[1]) + "\n" +
           "In Shelter:       " + str(n[2]) + "\n" +
           "In Foster:        " + str(n[3]) + "\n" +
           "Rescue-Reclaim:   " + str(n[4])  + "\n" +
           "Total:            " + str(n[5])
        )   
    
    print(tbl,file=fn)
    fn.close()
    """
    print("Category Count Completed")
    
        # Create a figure with two subplots
    fig = plt.subplots(figsize=(5,5))
    
    tstr = 'All of Today\'s Shelter Animals (' + str(countF) + ') by Category '
    palette_color = sns.color_palette('colorblind') 
    plt.pie(plt_data, labels=keys, colors=palette_color, autopct='%.0f%%', explode=[0.05, 0.05, 0.05, 0.05, 0.05]) 
    plt.title(tstr)
    #plt.show()
    plt.savefig(fs_category)

    return countF            
    
# use
if __name__ == '__main__':  # This will run if the file is run directly 
    dbase = 'acc_animals.db' 
    path = 'html/plots/'
    cf = category_pie_chart(dbase,path)
    print(cf)