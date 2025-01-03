
import httpx
import re
import codecs
from selectolax.parser import HTMLParser
import random

def get_cat_quote(txt_path):
    """
    Purpose: Generate quote of the day text file to include in the About Page
    """
    fname = txt_path + 'cat_quote.txt' # text file to be concatenated into "About" page
    f = open(fname,"w", encoding= "ISO-8859-1")
    
    nth_page = random.randint(1,43);  # Choose at random from the 44 pages 
    urlb = 'https://www.goodreads.com/quotes/tag/cats?page='
    url = urlb + str(nth_page)

    #url = 'https://www.goodreads.com/quotes/tag/cats'

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

    resp = httpx.get(url,headers=headers)

    html=HTMLParser(resp.text)

    q = (html.css('div.quoteText'))  # Get the number of quotes on the page
    nquote = random.randint(1,len(q)-1)  # Choose a random quote from the page
    
    quote = (q[nquote]).text()  #  The selected quote in a (unicode) char set    
    aquote = quote.encode("ISO-8859-1",errors='replace')  # changes the non utf-8 (Bytes)    
    bquote = aquote.decode("ISO-8859-1",errors='replace') # returns a utf-8 string
    
    cquote = bquote.replace('?', '"',2)  # Replaces first two question marks w/ ""    
    dquote = cquote.replace('?', '-')   # Replaces the 3rd ? with -
                                        # Note em dash is unicode NOT ISO-8859
    # equote = dquote.split("-")[0]  # to save the quote and author seperately
    # fquote = dquote.split("-")[1]  # and print with the p tag and pre tag for crlf's
    
    print(dquote,file = f)
    # print(equote)
    # print(fquote)
# Use
if __name__ == '__main__':  # This will run if the file is run directly
   #txt_path = 'html/html_inputs/'
    txt_path = ''
    get_cat_quote(txt_path)