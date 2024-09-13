#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Imports
from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint
import requests
import twilio

AMADEUS_API_KEY = 'JhAXlCXz9IGS5wk96gpQEo7MXBzk2N15'
AMADEUS_API_SECRET = '39WGiTWcON0SiDaf'
AMADEUS_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'

amadeus_params = {
    "client_id": AMADEUS_API_KEY,
    "client_secret": AMADEUS_API_SECRET,
}

amadeus_header = {
    'Content_Type': 'application/x-www-form-urlencoded'
}

SHEET_ENDPOINT = 'https://api.sheety.co/3d6c2f0d215852511aa284b0b7e45fa4/flightDeals/prices'


response = requests.get(SHEET_ENDPOINT)
sheet_data = response.json()

for data in sheet_data['prices']:
    # pprint(data)
    id = data['id']
    city = data['city']
    iataCode = data['iataCode']
    if not iataCode:
        flightSearch = FlightSearch(city)
        flight_data = DataManager(data)
        sheet_body = {
            'price': {
                "iataCode": flightSearch.get_iaticode()
            }
        }
        pprint(flight_data)
        # response = requests.put(f"{SHEET_ENDPOINT}/{id}", json=sheet_body)
        # pprint(response.json())

response = requests.get(SHEET_ENDPOINT)
# pprint(response.json())
