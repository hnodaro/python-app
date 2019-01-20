import requests
import urllib.request
from models.App import *
from bs4 import BeautifulSoup

class AppScrapper:

    # Scrapp data from the url
    def Scrapp(url):
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
            name=soup.find('h1', attrs={'class':'header__title'})
            version=soup.find('span', attrs={'itemprop':'version'})
            description=soup.find('p', attrs={'itemprop':'description'})
            releaseDate=soup.find_all('tr', attrs={'class':'app-info__row'})
            rel=releaseDate[4].find_all("td")

            downloadsNumber=releaseDate[2].find_all("td")
            rel=rel[1].text.strip()
            downloadsNumber=downloadsNumber[1].text.strip()
            name=name.text.strip()
            version=version.text.strip()
            description=description.text.strip()
            app = App(name,version,downloadsNumber,rel,description)
            return app
        

        
