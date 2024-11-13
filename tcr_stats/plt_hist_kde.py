
import datetime as dt
import statistics as stat 
import matplotlib.pyplot as plt
import seaborn as sns

def plt_hist_kde(type, list1, list2, label1='List 1', label2='List 2', bins=10, xlabel='Value', ylabel='Density'):
    # args = [type, list1, list2, label1='List 1', label2='List 2', bins=10, xlabel='Value', ylabel='Density']
    """
    Parameters:
    - type:  age plot or LOS plot
    - list1: First list of values to plot.
    - list2: Second list of values to plot.
    - label1: Label for the first list.
    - label2: Label for the second list.
    - bins: Number of bins for the histograms.
    - title: The overall title of the figure.
    - xlabel: The label for the x-axis.
    - ylabel: The label for the y-axis.
    """
        
    d0 = dt.date.today().isoformat()
    td = dt.date.today()
    t = td.strftime('%m/%d/%Y')  
    
    #  Probably need to create a seperate function for this with a return [type, title, fplot]
    # E.g.  plt_type =  ['AGE', "Distribution of Male and Female Cats Ages ", 'stats/Cat Ages_']
    # so  type = plt_type[0], tlte =  plt_type[1], fplt = plt_type[2]
    
    if type == 'AGE':
        title = "Distribution of Male and Female Cats Ages " + t
        fplot = 'html/outputs/Cat_Ages_' + d0 + '.png'
    elif type == 'LOS':
        title = "Distribution of Male and Female Cats Length of Stay (LOS) " + t
        fplot = 'html/outputs/Cat_LOS_' + d0 + '.png' 

    med1 = stat.median(list1) 
    med2 = stat.median(list2)
        
    print(fplot)
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the first list with histogram and KDE
    sns.histplot(list1, bins=bins, kde=True, ax=axes[0], color='skyblue')

    text_y = 0.9*axes[0].get_ylim()[1]
    axes[0].axvline(x =float(med1), color = 'g', label =  'Median', linestyle = '--')
    axes[0].text(med1, text_y, ' <----Median = '+str(med1)+ ' Days', fontsize = 12)

    axes[0].set_title(label1)
    axes[0].set_xlabel(xlabel)
    axes[0].set_ylabel(ylabel)
    axes[0].grid(True)  # Add gridlines to the first plot

    # Plot the second list with histogram and KDE
    sns.histplot(list2, bins=bins, kde=True, ax=axes[1], color='salmon')
    
    text_y = 0.9*axes[1].get_ylim()[1]
    axes[1].axvline(x =float(med2), color = 'g', label =  'Median', linestyle = '--')
    axes[1].text(med2, text_y, ' <----Median = '+str(med2)+ ' Days', fontsize = 12)

    axes[1].set_title(label2)
    axes[1].set_xlabel(xlabel)
    axes[1].set_ylabel(ylabel)
    axes[1].grid(True)  # Add gridlines to the second plot

    # Overall title
    plt.suptitle(title)    # override fcn argument to get date into title
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to make room for the title
    
    #plt.show()
    plt.savefig(fplot)

    # Create html text for modal plot images of AGE and LOS   TBD make this a seperate function... 
    # constants
    tab1 = '    '
    tab2 = '        '
    NL    = '\n'
    altEq = ' alt = '

    fname =  "html/imodal_" + type + ".txt"                # stat images
    f = open(fname,"w", encoding = "utf-8")   # open data file for text ouput

    a0 = tab1+'<img class =' + '\"' + 'myImages' + '\"' + NL
    a1 = tab2+'id= '+'\"' + 'myImg' + '\"' + ' src=' +'\"' + '../'+ fplot + '\"' + NL
    a2 = tab2+altEq+'\"'+ type +'\"'+' width='+'\"'+'50'+'\"'+' height=' '\"'+'50'+'\"'+ '>'


    html_str = a0+a1+a2
    print(html_str,file= f)

    f.close() 