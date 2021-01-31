from django.shortcuts import render
from django.http import HttpResponse
from .scripts import utilities
from _thread import start_new_thread

import threading
def index(request):
    return render(request, "PriceTracker/index.html")


# amazon input page function
def amazon_input(request):
    return render(request, "PriceTracker/amazoninput.html")


# flipkart input page function
def flipkart_input(request):
    return render(request, "PriceTracker/flipkartinput.html")


# ebay input page function
def ebay_input(request):
    return render(request, "PriceTracker/ebayinput.html")


def error(request):
    return render(request, "PriceTracker/error.html", )


def result(request, website):
    message = ""
    datadict = {}

    if request.method == "POST":
        url = request.POST["url"]
        desired_price = float(request.POST["desired_price"])
        email = request.POST["email"]
        in_range, datadict = utilities.scrape(website, url, desired_price, email)
        if in_range:
            message = "Hurry! price is in your desired range"
        else:
            message = "Not in your desired range :("
            utilities.saveData(website, url, desired_price, email)

    return render(request, "PriceTracker/result.html", {in_range: in_range, "message": message, "product_price": datadict["price"], '''
                                                          '''  "product_name": datadict['title'], "link": url},)


