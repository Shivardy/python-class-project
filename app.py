# Importing libraries and files.
from flask import Flask, render_template, request, send_file, url_for
from fetchimages import getImages, deleteImages
from encrpt_decrypt import encryption, decryption

# initializing the app.
app = Flask(__name__)

# defining the route to main page and loading index.html


@app.route('/')
def index():
    return render_template("index.html")  # returing index.html file

# defining the route to /encrypt


@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    # checking if the url path has message and image set
    if request.args.get("message") and request.args.get("image"):
        message = request.args.get("message")
        image = request.args.get("image")
        try:
            # calling enryption function with message and image source
            image = encryption(message, "https://source.unsplash.com/"+image)
            # function to delete previous images in the images directory
            deleteImages()
            # returning image as output
            return image
        except Exception as e:
            # if any error returning the error string
            return str(e)
    # rendering initial encrypt.html file with the images
    return render_template("encrypt.html", images=getImages())

# defining loadmore button and its function.


@app.route('/loadmore', methods=['GET', 'POST'])
def loadmore():
    if request.method == "POST":
        # returning html template with more image data.
        return render_template("loadmoreimages.html", images=getImages())


# defining downloadimage button and its funciton
@app.route('/downloadimage', methods=['GET', 'POST'])
def downloadimage():
    # checking for the id in the url path
    if request.args.get("id"):
        # retuning the image with that partucular id.
        return send_file("images/"+request.args.get("id"), attachment_filename="encrypted.jpg")


# defining /decrypt path and loading decrypt.html


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    message = ""
    # checking if the image is uploaded or not
    if request.method == 'POST':
        # accessing the file
        file = request.files['file']
        # saving the file
        file.save("images/"+file.filename)
        try:
            # function to delete previous images in the images directory
            deleteImages()
            # calling decyrption function with the filename
            message = decryption(file.filename)
        except:
            message = "error"
            # rendering decrypt.html template
        return render_template("decrypt.html", message=message)
    return render_template("decrypt.html", message=message)

# defining /about path


@app.route('/about')
def about():
    # rendering about.html page
    return render_template("about.html")


# checking for 404 page not found error
@app.errorhandler(404)
def page_not_found(e):
    # rendering custom 404 message
    return render_template('error.html')


# defining the main.
if __name__ == '__main__':
    # running the app.
    app.run(debug=True)
