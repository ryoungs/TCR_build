from PIL import Image, ImageDraw, ImageFont

def prep_img(img, name, sexage):
    """Function generate Background and Captions:  Name, Sex, and Age."""
    img_w, img_h = img.size
    # prepare a color background for text "overlay"
    # Image is 600 x 450 (static from AACACC Website)
    # Add 100 px top and bottom for text
    bg_w = img_w
    bg_h = img_h + 200
    bg_size = (bg_w,bg_h)
    bg_color = (80,15,140)
    background = Image.new('RGB', bg_size, bg_color)
    # Center the imgage over the background 
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    draw = ImageDraw.Draw(background)
    # Put the name in text On Top
    my_font = ImageFont.truetype('arialbd.ttf', 45)
    _, _, w, h = draw.textbbox((0, 0),name, font=my_font)
    draw.text(((img_w-w)/2, (img_h-h)/2-175), name, font=my_font, fill='yellow', align='center')
    # Put the Sex and Age (variable sexage) in text On Bottom
    _, _, w, h = draw.textbbox((0, 0),sexage, font=my_font)
    draw.text(((img_w-w)/2, (img_h-h)/2+375), sexage, font=my_font, fill='yellow', align='center')
    return background