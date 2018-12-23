# loading libraries
import urllib.request
import json
import glob
import os

# function definition


def getImages():
    # initializing apikey and source url
    apikey = "28b5aa0a159f0ffa62f4b302db01c72b289c551e5b6cf81ca9d88310dcfad414"
    url = "https://api.unsplash.com/photos/random?count=8&orientation=squarish&featured=true&client_id="+apikey
    try:
        # calling the api and geting the response
        response = urllib.request.urlopen(url)
    except:
        return "failed"
    else:
        # converting the data into json format
        data = json.load(response)
        # filtering out the id,url from the json data
        imageRegularSize = [[i["id"], i["urls"]["small"]] for i in data]
        # returning the image data
        return imageRegularSize


def deleteImages():
    # listing the files in images directory
    files = glob.glob("images/*")
    # sorting the files based on creation time
    files.sort(key=os.path.getmtime)
    # reversing the list
    files = files[::-1]
    # deleting all the files except the recent 10 files.
    for i in files[10:]:
        os.unlink(i)
