from PIL import Image, ImageTk
from io import BytesIO
import sqlite3

con = sqlite3.connect('acc_animals.db')

def show(data):
    img_byte = BytesIO(data)
    img_byte.show()

    
    
def fetch(id):
    c = con.cursor()
    c.execute('SELECT image_acc FROM animals where id=?',(id,))
    data = c.fetchall()[0][0] # Get the blob data
    show(data) # Call the function with the passes data
    
    
fetch(1)