Title : Image Stegnography
Developer : Shiva Reddy

Introduction :-
This is flask based client server application which helps us to encrypt and decrypt a message inside
an image.

Setup :-
Install and import the following libraries.
1) Flask :- pip install flask (http://flask.pocoo.org/docs/1.0/installation/) 
2) PIL :- pip install pillow  (https://pypi.org/project/Pillow/2.2.1/)

Execution :-
1) Open python terminal and navigate to project directory.
2) Run the following command: python app.py
3) The program outputs a URL and now open that URL in a browser.

Project Architecture :-
/ Main-Directory       
        App.py (Main function __init.py__)
        Encrypt_Decrypt.py (program to encrypt and decrypt message)
        FetchImages.py (program to fetch images from API)
        / Static   
                main.js (All the javascript)
                main.css (All the CSS)
                Images (All the static images used in the project)
        /  Templates
                / Includes
                        Header.html
                        Footer.html
                About.html
                Decrypt.html        
                Encrypt.html
                Error.html      
                Index.html
                Layout.html
                Loadmoreimages.html        
        / Images
                …… All uploaded images, downloaded images from API
        

Program File Description:-
1)  App.py :- This is the init file from where the execution starts and this file initiates the server and handles
    all the routes like /encrypt, /decrypt of the application.
2)  Encrypt_Decrypt.py :- This file contains the encryption and decryption logic and it manupulates the image files
    to store and retrive message.
3)  FetchImages.py :- This file makes calls to the online image api to fetch images and serves to the application.
4)  Main.js :- This file contains all the javascript which handles the user inputs on the application and dynamically
    renders the content based on user click, it makes requests to the server and update the webpage with the response
    from the server.
5)  Main.css :- This contains all the styling elements of the application.
6)  templates/*.html :- All the html files contain the static html content which is neccessary to hold the data and provide 
    user interface, all these files contain basic html.
7)  templates/includes/*.html :- This folder contains the static footer and header of the application.
8)  images :- This directory contains the downloaded image when you select an image for encryption and even contains the
    images you upload for decryption.
9)  static :- This directory contains the static images, css, javascript used in this application.
