from time import sleep

from django.apps import AppConfig
import threading


class PricetrackerConfig(AppConfig):
    name = 'PriceTracker'
    def ready(self):
        from .scheduler import scheduler
        th = threading.Thread(target=scheduler.scheduleScrape)
        th.start()









