from flask import Flask, render_template, request
import services.scrapper 
import requests
import re

app = Flask(__name__)

# Check if the url is valid (https://app-name.xx.aptoide.com)   
def isUrl(url):
    pattern="http[s]*:\/\/[a-zA-Z0-9_-]*\.\w{2}\.(aptoide\.com)"
    exp=re.compile(pattern).search(url)
    if exp != None:
        return True
    else:
        return False

#Check if the website is up
def isUp(url):
    r = requests.head(url)
    if r.status_code == 200:
        return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =='POST':
        #Get url typed by user
        url=request.form['url'].lower()
        #If url is valid
        if isUrl(url):
            if isUp(url):
                #Scrapp data from the url
                app=services.scrapper.AppScrapper.Scrapp(url)
                #Return the view
                return render_template('app.html', name=app.name, version=app.version, downloads=app.downloadsNumber, release=app.release, description=app.description)
            else:
                err="Error: Url doesn't exist"
                return render_template('home.html', error=err)
        else:
            err="Please submit a valid aptoide URL"
            return render_template('home.html', error=err)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=False)


