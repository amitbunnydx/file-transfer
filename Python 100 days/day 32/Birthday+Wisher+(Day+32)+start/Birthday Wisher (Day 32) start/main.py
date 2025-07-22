import smtplib
import datetime as dt
import random

my_email="amitworkingid@gmail.com"
to_email="amit04838@gmail.com" #"supriyagaikwad18898@gmail.com" #"amit04838@gmail.com",
password="wftihharhkymlgro"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com",587,timeout=120) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Morning Quotes \n\n {random_quotes}")

# now=dt.datetime.now()
# year=now.year
# day=now.day
# month=now.month
# dayofweek=now.weekday()
# print(dayofweek)

# quotes sending mail

now=dt.datetime.now()
weekdays=now.weekday()
print(weekdays)
if weekdays==4:
    print(now)

    with open('quotes.txt','r') as quotes:
        quotes_list=[quotes for quotes in quotes.readlines()]
    print(quotes_list)
    random_quotes=random.choice(quotes_list)
    print(random_quotes)
    send_mail()