import sqlite3
import matplotlib.pyplot as plt
import pandas as pd 
import statistics as stat
from datetime import datetime, date
import seaborn as sns
from PIL import Image, ImageDraw, ImageFont
from sqlite_utils import Database
from pandas.plotting import table

def plot_hist_kde(type, path, list1, list2, label1="List 1", label2="List 2", bins=10, xlabel="Value", ylabel="Density"):
    """
    Parameters:
    - type:  age plot or LOS plot
    - path:  where to put *.png plots
    - list1: First list of values to plot.
    - list2: Second list of values to plot.
    - label1: Label for the first list.
    - label2: Label for the second list.
    - bins: Number of bins for the histograms.
    - title: The overall title of the figure.
    - xlabel: The label for the x-axis.
    - ylabel: The label for the y-axis.
    """
        
    d0 = date.today().isoformat()
    td = datetime.today()
    t = td.strftime('%m/%d/%Y')  
    
    #  Probably need to create a seperate function for this with a return [type, title, fplot]
    # E.g.  plt_type =  ['AGE', "Distribution of Male and Female Cats Ages ", 'stats/Cat Ages_']
    # so  type = plt_type[0], tlte =  plt_type[1], fplt = plt_type[2]
    
    med1 = stat.median(list1)
    med2 = stat.median(list2)
    
    if type == 'AGE':
        title = "Distribution of Male and Female Cats Ages " + t
        fplot = path + 'Cat_Ages_' + d0 + '.png'
        txt = ' Years'
        txtp1 = f"<---Median {med1:.2f}" + txt
        txtp2 = f"<---Median {med2:.2f}" + txt
    elif type == 'LOS':
        title = "Distribution of Male and Female Cats Length of Stay (LOS) " + t
        fplot = path + 'Cat_LOS_' + d0 + '.png'
        txt = ' Days'
        txtp1 = f"<---Median {med1:.2f}" + txt
        txtp2 = f"<---Median {med2:.2f}" + txt

    # print(fplot, med1, med2)
    
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the first list with histogram and KDE
    sns.histplot(list1, bins=bins, kde=True, ax=ax1, color='skyblue')
    text_y = 0.9*ax1.get_ylim()[1]
    ax1.axvline(x =float(med1), color = 'g', label =  'Median', linestyle = '--')
    ax1.text(med1, text_y,txtp1 ,fontsize=12)
    ax1.set_title(label1)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.grid(True)  # Add gridlines to the first plot

    # Plot the second list with histogram and KDE
    sns.histplot(list2, bins=bins, kde=True, ax=ax2, color='salmon')
    text_y = 0.9*ax2.get_ylim()[1]
    ax2.axvline(x =float(med2), color = 'g', label =  'Median', linestyle = '--')
    ax2.text(med2, text_y,txtp2,fontsize=12)
    ax2.set_title(label2)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel)
    ax2.grid(True)  # Add gridlines to the second plot

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