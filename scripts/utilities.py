from mails import *
from webscrape import *
import datetime
from fileIO import *
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
        print("Avalability: " + datadict['availability'])
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

    presenttime = datetime.datetime.now()
    #write data to file with new time
    fileWrite(website, link, str(desired_price), receiver, presenttime.strftime('%Y/%m/%d %H:%M:%S'))
    return in_range, datadict
