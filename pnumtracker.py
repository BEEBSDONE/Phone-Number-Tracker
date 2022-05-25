import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim

def track():
    
    target = input("Enter the target: ")

    number = phonenumbers.parse(target)
    locate = geocoder.description_for_number(number, 'en')
    print(locate)

    operator = carrier.name_for_number(number, 'en')
    print(operator)

    time = timezone.time_zones_for_number(number)
    print(time)

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate)
    lng = location.longitude
    lat = location.latitude
    print("Longitude:", lng)
    print("Latitude:", lat)

track()