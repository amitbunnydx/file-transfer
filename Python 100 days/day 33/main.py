import time
from http.client import responses
#
import requests
from datetime import *
import smtplib
import time


my_email="amitworkingid@gmail.com"
to_email="amit04838@gmail.com" #"supriyagaikwad18898@gmail.com" #"amit04838@gmail.com",
password="lznqzwtkhpticthk"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com",587,timeout=120) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:LOOK UP \n\n look up in the sky there is iss")

my_lat=19.075983
my_long=72.877655

def comapir_disct():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if my_lat-5 <=iss_latitude<=my_lat+5 and my_long-5<=iss_longitude<=my_long+5:
        return True

def insnight():
    parameters={
        'lat':my_lat,
        'lng':my_long,
        "formatted":0,
    }
    response=requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(':')[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(':')[0])
    print(sunrise)
    print(sunset)
    time_now=datetime.now().hour
    if time_now<=sunrise or time_now>=sunset:
        return True

while True:
    time.sleep(60)
    if  insnight() and comapir_disct():
        send_mail()




