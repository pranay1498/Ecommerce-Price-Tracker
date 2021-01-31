from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
from PriceTracker import models
from PriceTracker.scripts import utilities, mails


# schedule helper function to loop through all rows of a model
def scheduleHelp(all_objects, website):
    for each in all_objects:
        url = each.URL
        email = each.email
        desired_price = each.desired_price
        in_range, datadict = utilities.scrape(website, url, desired_price, email)
        if in_range:
            each.delete()


# main scheduler function
def scheduleScrape():
    scheduleHelp(models.Amazon.objects.all(), 'AMAZON')
    scheduleHelp(models.Flipkart.objects.all(), 'FLIPKART')
    scheduleHelp(models.Ebay.objects.all(), 'EBAY')


def start():
    backscheduler = BackgroundScheduler()
    backscheduler.add_jobstore(DjangoJobStore(), "default")
    backscheduler.add_job(scheduleScrape(), 'interval', seconds=30, name='scrape_all', jobstore='default')
    backscheduler.start()

