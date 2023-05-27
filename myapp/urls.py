# myapp/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/scrape/', ApiVIewScrap.as_view()),
    path('api/v2/scrape/', ScrapeDataView.as_view()),

]
