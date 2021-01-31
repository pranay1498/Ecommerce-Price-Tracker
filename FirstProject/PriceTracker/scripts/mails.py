import smtplib
from django.core.mail import send_mail
from FirstProject import settings
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from PriceTracker import views


def sendMail(datadict, product_link, receiver):
    subject = "Your product is in range"
    to = receiver
    body = f'product name: {datadict["title"]} \n' \
           f'product price: {datadict["price"]} \n' \
           f'{datadict["availability"]} \n' \
           f'product link: {product_link}'
    res = send_mail(subject, body, settings.EMAIL_HOST_USER, [to])
    if res != 1:
        return render(HttpRequest, "PriceTracker/error.html", {"message": "Mail could not be sent"})
