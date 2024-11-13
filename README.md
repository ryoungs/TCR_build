<h2><center>The Cat Room Build Project (TCR_build)</center></h2> 
<p>Create a script that builds "The Cat Room" (Static) Web Page for Anne Arundel County Animal Care and Control (AACACC) Cats</p> 
<p>Echo AACACC list of Cats available for adoption in a different format that is quicker and easier to access</p>

## Objective
* Automated web page updates for AACACC adoptable cats
* Pull ACC data and images to a local database
* Marquee struggling cats with photos and videos
* Expand social media marketing

## Features
* Scrape AACACC animal data for basic data and base image
* Insert the data into a database (acc_animals.db)
* Process the base image to add name, sex, age captions
* Add the processed image REPO path to the database 
* Class library of web automation related functions
* Test modules for each function
* Daily update (recreate) a main page with captioned images in a grid
* Publish a weekly contact sheet 

## Plans
* Create HTML and CSS files to publish adoptable pets
* Powershell script launches daily updates
* Push updates to social media sites 
* Updade & improve code modularization, add error processing
* Add features <pre> 
    Lost and found and foster pages
    archive adoption and foster data 
    Add sorting / filtering to Lightbox2 image gallery
    Cage cards with QR codes
    </pre> 

## Build Sequence
<ol>
    <li>Backup database and clean published files
    <li>Scrape AACACC online data
    <li>Populate new database 
    <li>Add numeric fields
    <li>Add background and captions to images
    <li>Create some statistical plots
    <li>Create html elements for sections and Lightbox2 gallery
    <li>Concatenate html elements into Home & Foster html pages
    <li>Publish to Github REPO 

# TBD
* Add javascript/jQuery sort/filter/hide-show function
* Add more statistics - revise Home page
* Add more proactive social media updating
* Add function to put preped images onto html grid
* Add "Cat of the Day" and/or Cat-quote of the day 
* Add automated testing / try-except to functions
* Migrate to a new host (Netlify ?)

