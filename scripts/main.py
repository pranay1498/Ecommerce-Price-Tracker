import time
from utilities import *

REPEAT_TIME = datetime.timedelta(seconds=10)    #time for repeating the task
websites = ['AMAZON', 'FLIPKART', 'EBAY']   #websites which our script works on


choice = input("enter 1 for new link \nenter 2 for same link\n")

if choice == '1':
    website_choice = int( input("AMAZON (enter 1) \nFLIPKART (enter 2) \nEBAY (enter 3)\n") )

    #take inputs from user
    link = input("enter product link: ")
    desired_price = int(input("enter desired price:"))
    receiver = input("enter your mail id:")

    # dictionary to store product details
    datadict = {}

    if website_choice not in (1, 2, 3):
        print("invalid entry....closing program")
        exit(0)

    in_range, datadict = scrape(websites[website_choice - 1], link, desired_price, receiver)

    #print product details and if in range or not
    printInfo(datadict, in_range)

    #exit if product in range
    if in_range:
        exit(0)


elif choice == '2':
    infodict = fileRead()

    #take previous time form
    previous_time = datetime.datetime.strptime(infodict['time'], '%Y/%m/%d %H:%M:%S')

    website_choice = infodict['website']
    link = infodict['link']
    desired_price = int(infodict['price'])
    receiver = infodict['mail']

    #check if repeat time exceeded
    if (datetime.datetime.now() - previous_time) >= REPEAT_TIME:
        in_range, datadict = scrape(website_choice, link, desired_price, receiver)
        printInfo(datadict, in_range)
        if in_range:
            exit(0)


#loop to keep script running
while True:
    infodict = fileRead()

    # take previous time form
    previous_time = datetime.datetime.strptime(infodict['time'], '%Y/%m/%d %H:%M:%S')

    website_choice = infodict['website']
    link = infodict['link']
    desired_price = int(infodict['price'])
    receiver = infodict['mail']


    #sleep for the specified repeat time
    while (datetime.datetime.now() - previous_time) < REPEAT_TIME:
        time.sleep(1)

    in_range, datadict = scrape(website_choice, link, desired_price, receiver)
    #not printing when looping, only printing when script starts every time

    # exit if product in range
    if in_range:
        exit(0)

