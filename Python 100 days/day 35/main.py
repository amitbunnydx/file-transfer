import requests
from pandas.tseries.holiday import weekend_to_monday

api_key="31f8e694058349672e01477e2c340072"
OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"

my_lat=-5.137319
my_long=119.428242

parameter={
"lat":my_lat,
 "lon":my_long,
    "cnt":4,
    "appid":api_key
}

response=requests.get(OWM_Endpoint,params=parameter)
print(response.status_code)
response.raise_for_status()
print(response.json())
data=response.json()["list"]
for data in data:
    weather=data["weather"][0]["id"]
    if int(weather)<700:
        print("bring the umbrella")
    else:
        print("no need to bring umbrella")
    print("\n")
# print(data)