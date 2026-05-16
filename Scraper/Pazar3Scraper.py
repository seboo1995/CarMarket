import requests
from bs4 import BeautifulSoup
from utils import readConfig

def readConfigForPazar3():
    config = readConfig('Pazar3')
    return config

class Pazar3Scraper():

    def __init__(self):
        self. config = readConfigForPazar3()
        self.startingURL = self.config['startingURL']
        self.numOfPages = self.config['pages']
        self.selectors = self.config['selectors']
    def __createListOfURLs(self):
        res = []
        for i in range(1,int(self.numOfPages)):
            sURL = self.startingURL+str(i)
            res.append(sURL)
        return res


    def __getResponse(self,URL):
        response = requests.get(URL)
        if response.status_code != 200:
            raise ValueError(f'Page {URL} could not be scraped because of response.Response gotten: {response.status_code}')

        return response

    def __loadSoupFromPage(self,URL):
        response = self.__getResponse(URL)
        soup = BeautifulSoup(response.text)
        return soup

    def getSelector(self,name):

        if name in self.selectors:
            return self.selectors[name]
        else:

            raise ValueError('getSelectors: no selector found named: {name})')
    def __scrapePage(self,sURL):
        soup = self.__loadSoupFromPage(sURL)
        listing_selector =self.selectors['AdSelector']
        all_listings_in_page = soup.select(listing_selector)
        res = []
        for listing in all_listings_in_page:
            titleSelector = self.selectors['titleSelector']
            title = listing.select(titleSelector)[0].text
            price =




    def getAllListings(self,soup):





    def scrapeAll(self):
        links = self.__createListOfURLs()

        for link in links:
            pass







