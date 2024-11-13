from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import pandas as pd 
from pandas.plotting import table

def plot_cat_dog_table(fname, cat_total, dog_total):

    # II ---------------- Create Side by Side table of Cat and Dog Totals ---------
    
    print("Cats: "+str(cat_total) + " Dogs: " + str(dog_total))

    # grand_total = count_category()  # Gets category data from allacc.db, plots pie chart
    # print("Grand Total = " + str(grand_total))

    data1 = {
        'Category': ['Males', 'Females', 'Altered', 'Strays','Given-up','Unassigned','Total'],
        'Count': cat_total
    }

    data2 = {
        'Category': ['Males', 'Females', 'Altered', 'Strays','Given-up','Unassigned','Total'],
        'Count': dog_total
    }

    save_tables_as_image(data1, data2, fname, title1="All Cats Today", title2="All Dogs Today")


def save_tables_as_image(data1, data2, filename, title1=None, title2=None):
    # Convert data to DataFrame if it is not already one
    if not isinstance(data1, pd.DataFrame):
        data1 = pd.DataFrame(data1)
    if not isinstance(data2, pd.DataFrame):
        data2 = pd.DataFrame(data2)

    # Hide the index if specified
    #data1.reset_index(drop=True, inplace=True)
    #data2.reset_index(drop=True, inplace=True)
    data1.style.format("{:,.1f}").hide(level=1)
    data2.style.format("{:,.1f}").hide(level=1)

    # Create a plot with two subplots side by side
    fig, axes = plt.subplots(1, 2, figsize=(5, 3))

    # First table
    if title1:
        axes[0].set_title(title1, fontdict={'fontsize': 16, 'fontweight': 'bold'}, pad=20)
        axes[0].xaxis.set_visible(False)
        axes[0].yaxis.set_visible(False)
        axes[0].set_frame_on(False)
        tab1 = table(axes[0], data1, loc='center', cellLoc='center')
        tab1.auto_set_font_size(False)
        tab1.set_fontsize(12)
        tab1.scale(1.2, 1.6)  # Scale the table to make it bigger

    # Second table
    if title2:
        axes[1].set_title(title2, fontdict={'fontsize': 16, 'fontweight': 'bold'}, pad=20)
        axes[1].xaxis.set_visible(False)
        axes[1].yaxis.set_visible(False)
        axes[1].set_frame_on(False)
        tab2 = table(axes[1], data2, loc='center', cellLoc='center')
        tab2.auto_set_font_size(False)
        tab2.set_fontsize(12)
        tab2.scale(1.2, 1.6)  # Scale the table to make it bigger

    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)

    # Convert the plot to an image
    img = Image.open(filename)
    img = img.convert("RGB")  # Ensure it's an RGB image
    
    # Save as PNG image
    img.save(filename, format='PNG')

    # Close the plot
    plt.close()