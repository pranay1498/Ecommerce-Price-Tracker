from .mails import *
from .webscrape import *
import datetime
from PriceTracker import models
#few helper functions

WEBSITES = ['AMAZON', 'FLIPKART', 'EBAY']

#check if price is in range

def checkPrice(desired, actual):
    return actual <= desired


#to print the data

def printInfo(datadict, in_range):
    print("Product name: " + datadict['title'])
    print("Current price: " + str(datadict['price']))
    if datadict['availability'] != '':
        print("Availability: " + datadict['availability'])
    if in_range:
        print("Product is in your desired range!!")
    else:
        print("Product is not in your desired range :(")


#function for scraping data and sending mail if price in range, return boolean if price in range or not

def scrape(website, link, desired_price, receiver):
    if website == WEBSITES[0]:
        datadict = scrapeAmazon(link)
    elif website == WEBSITES[1]:
        datadict = scrapeFlipkart(link)
    elif website == WEBSITES[2]:
        datadict = scrapeEbay(link)

    # check if product is in range
    in_range = checkPrice(desired_price, datadict['price'])

    # if product is in range then send mail
    if in_range:
        sendMail(datadict, link, receiver)

    return in_range, datadict


# function to save data in datatbase
def saveData(website, link, desired_price, email):
    obj = None
    if website == WEBSITES[0]:
        obj = models.Amazon(URL=link, desired_price=desired_price, email=email, time = datetime.datetime.now())
    elif website == WEBSITES[1]:
        obj = models.Flipkart(URL=link, desired_price=desired_price, email=email, time=datetime.datetime.now())
    elif website == WEBSITES[2]:
        obj = models.Ebay(URL=link, desired_price=desired_price, email=email, time=datetime.datetime.now())
    obj.save()

