import plotly.graph_objects as go
import plotly.express as px
import kaleido
import pandas as pd
from datetime import datetime, date
import sqlite3
from sqlite_utils import Database


def stacked_category_bar(path):

    d0 = date.today().isoformat()
    fs_category = path + 'System_' + d0 + '.png'  
    
    db = Database('acc_animals.db')

    # All animals
    A0 =  db["animals"].count_where("firstChoiceMessage = ?", ['ADOPTION PENDING',])
    B0 =  db["animals"].count_where("firstChoiceMessage = ?", ['ADOPTION PENDING (OFFSITE)',])
    C0 =  db["animals"].count_where("firstChoiceMessage = ?", ['ASK TO VISIT ME AT THE SHELTER',])
    D0 =  db["animals"].count_where("firstChoiceMessage = ?", ['IN FOSTER CARE - ASK HOW TO MEET ME',])
    E0 =  db["animals"].count_where("firstChoiceMessage = ?", ['',])  # RESCUE / RECLAIM

    # Cats
    A1 =  db["animals"].count_where("species = 'CAT' and firstChoiceMessage = ?", ['ADOPTION PENDING',])
    B1 =  db["animals"].count_where("species = 'CAT' and firstChoiceMessage = ?", ['ADOPTION PENDING (OFFSITE)',])
    C1 =  db["animals"].count_where("species = 'CAT' and firstChoiceMessage = ?", ['ASK TO VISIT ME AT THE SHELTER',])
    D1 =  db["animals"].count_where("species = 'CAT' and firstChoiceMessage = ?", ['IN FOSTER CARE - ASK HOW TO MEET ME',])
    E1 =  db["animals"].count_where("species = 'CAT' and firstChoiceMessage = ?", ['',])

    # Dogs
    A2 =  db["animals"].count_where("species = 'DOG' and firstChoiceMessage = ?", ['ADOPTION PENDING',])
    B2 =  db["animals"].count_where("species = 'DOG' and firstChoiceMessage = ?", ['ADOPTION PENDING (OFFSITE)',])
    C2 =  db["animals"].count_where("species = 'DOG' and firstChoiceMessage = ?", ['ASK TO VISIT ME AT THE SHELTER',])
    D2 =  db["animals"].count_where("species = 'DOG' and firstChoiceMessage = ?", ['IN FOSTER CARE - ASK HOW TO MEET ME',])
    E2 =  db["animals"].count_where("species = 'DOG' and firstChoiceMessage = ?", ['',])

    """ print([A0, B0,C0,D0,E0])
        print([A1, B1,C1,D1,E1])
        print([A2, B2,C2,D2,E2])"""
    
    keys = ['Pending Adopt','Foster to Adopt','Adoptable','In Foster','Rescue-Reclaim']   
    plt_data = {'Category': ['All Pets','Cats','Dogs'], keys[0]: [A0,A1,A2],keys[1]: [B0,B1,B2],keys[2]: [C0,C1,C2],keys[3]: [D0,D1,D2],keys[4]: [E0,E1,E2] }     

    # Create a sample DataFrame
    # data = {'Category': ['A', 'B', 'C'], 'Value1': [10, 15, 20], 'Value2': [5, 10, 15]}
    df = pd.DataFrame(plt_data)
    # print(df)
    
    # OR
    df2 = pd.DataFrame([['All Pets','Adopt Pending',A0],['All Pets','Foster to Adopt',B0],['All Pets','Adoptable',C0],['All Pets','In Foster',D0],['All Pets','Rescue',E0],
                        ['Cats','Adopt Pending',A1],['Cats','Foster to Adopt',B1],['Cats','Adoptable',C1],['Cats','In Foster',D1],['Cats','Rescue',E1],
                        ['Dogs','Adopt Pending',A2],['Dogs','Foster to Adopt',B2],['Dogs','Adoptable',C2],['Dogs','In Foster',D2],['Dogs','Rescue',E2]],
                       columns = ['Pets','Category','Count'])
    
    fig = px.bar(df2, x="Pets", y="Count", color="Category",
                 width=1000, height=600,text_auto=True)
    fig.update_traces(width=0.5)
    
        # Update the layout
    fig.update_layout(
        title ={'text':'Number of Animals in the System Today','x':0.5,'xanchor':'center','yanchor':'top'},
        barmode='stack',
        xaxis_title='Category',
        yaxis_title='Animal Count',
        legend_title='Shelter Categories',
        font=dict(
            family="Arial Rounded MT",
            size=18,
            color="RebeccaPurple"
        ))
        
    # Show the plot
    fig.write_image(fs_category)
    #fig.show()
    # use"""
if __name__ == '__main__':  # This will run if the file is run directly 
    path = 'html/plots/'
    cf = stacked_category_bar(path)
#