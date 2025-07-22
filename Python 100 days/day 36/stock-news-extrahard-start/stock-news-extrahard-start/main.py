import requests
from datetime import *
import smtplib
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_endpoint="https://www.alphavantage.co/query"#?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo
my_email="amitworkingid@gmail.com"
to_email="amit04838@gmail.com" #"supriyagaikwad18898@gmail.com" #"amit04838@gmail.com",
password="lznqzwtkhpticthk"
Stock_apikey="DHZA5W0I5XPSU6LJ"
#to get raid of this error try to connect with different network
def send_mail(title, content, percent):
    with smtplib.SMTP("smtp.gmail.com",587,timeout=120) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:TSLA:  \n\n Headline: \n\n Brief:{content}")
                        # msg = f"Subject:Morning news \n\n {content}"    )

toda_date=datetime.now()
print(toda_date.date())
today = toda_date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=4)

yesterday_date=yesterday.date()
# yesterday_date="2029-02-04"
two_days_ago_date=day_before_yesterday.date()

parameters={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":Stock_apikey,
}
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=6ZKIGQ1O3W5VEIKJ'
r = requests.get(stock_endpoint,params=parameters)
# data = r.json()
# print(data)
print(r.text)
# daily_data=data['Time Series (Daily)']
# print(daily_data)
# for date_data, value in daily_data.item():
#     # print(date_data)
#     yesterday = today - timedelta(days=1)
#     day_before_yesterday = today - timedelta(days=4)
#     if str(yesterday.date()) in date_data:
#         print(value)
#         print('innn')
#     elif str(day_before_yesterday.date()) in date_data:
#         print('innn2')
#         print(value)

# try:
#     yesterday = today - timedelta(days=1)
#     final1=daily_data[str(yesterday.date())]["4. close"]
#     # print(final1)
# except:
#     print('data is not avilable')
# else:
#     day_before_yesterday = today - timedelta(days=4)
#     final2 = daily_data[str(day_before_yesterday.date())]["4. close"]
    # print(final2)

#news  of the data
def news_fun():
    parameters={
            'q':'Tesla',
            'from':yesterday_date,
            'sortBy':'popularity',
            'apiKey':"1959fa4e6f3c40eda160f6c1bdd002b0",
        }
    news_response=requests.get(url="https://newsapi.org/v2/everything",params=parameters)
    # print(news_response.json())
    news_data=news_response.json()
    # print(news_data['articles'])
    artical=title=news_data['articles']
    three_artical=artical[:3]
    print(three_artical)
    print("---------------------------------------------")
    for i in range(3):
        title=news_data['articles'][i]['title']
        # description=news_data['articles'][i]['description']
        content=news_data['articles'][i]['content'].encode("ascii", "ignore").decode()
        print(content)
        send_mail(title,content,int(n2))



num1=383.6800
num2=404.6000

final=num1-num2
n1=final/num2
n2=n1*100
print(int(n2))


if n2>=5 or n2<=-5:
    print('in')
    news_fun()




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

