from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("amazon", views.amazon_input, name='amazon'),
    path("flipkart", views.flipkart_input, name="flipkart"),
    path("ebay", views.ebay_input, name="ebay"),
    path("result/<str:website>", views.result, name="result"),
    path("error", views.error, name="error")
]

