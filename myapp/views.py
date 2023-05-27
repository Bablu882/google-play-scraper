from google_play_scraper import search
from itertools import islice
from django.http import HttpResponse
from .tasks import fetch_package_details
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Package

class ApiVIewScrap(APIView):
    @csrf_exempt
    def get(self, request, format=None):
        package_names = []
        count = 0  # Count of fetched package names

        for result in islice(search('game', country='us'), 50):  # Fetch a larger number of results
            if 'appId' in result:
                package_name = result['appId']
            elif 'bundleId' in result:
                package_name = result['bundleId']
            else:
                continue  # Skip this result if neither key is found

            package_names.append(package_name)
            count += 1

            if count >= 10:
                break

        # Fetch package details for each package name
        for package_name in package_names:
            print(package_name)
            package_details=fetch_package_details.delay(package_name)
            package = Package(name=package_name, details=package_details.get())
            package.save()

        return Response({'message':'Scraping queued.'})




###=================================================================================###

class ScrapeDataView(APIView):
    def post(self, request, format=None):
        #url = "https://play.google.com/store/games?hl=en&gl=US"
        url=request.data.get('url')
        if not url:
            return Response({'message':{'url required !'}})

        # Send a GET request to the URL and retrieve the HTML content
        response = requests.get(url)
        html_content = response.content

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract package names from the page
        package_elements = soup.select('div[data-item-id]')[:10]
        package_names = [element['data-item-id'] for element in package_elements]

        # Fetch package details for each package name
        for package_name in package_names:
            print(package_name)
            package_details = fetch_package_details.delay(package_name)
            package = Package(name=package_name, details=package_details.get())
            package.save()

        return Response({'message': 'Scraping queued.'})
