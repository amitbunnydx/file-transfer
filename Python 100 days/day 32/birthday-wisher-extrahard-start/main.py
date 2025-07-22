##################### Extra Hard Starting Project ######################
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import datetime as dt
import os
import smtplib


files=os.listdir("letter_templates/")

now=dt.datetime.now()
today_month=now.month
today_day=now.day

PLACEHOLDER= '[NAME]'

my_email="amitworkingid@gmail.com"
password="lznqzwtkhpticthk"

def send_mail(to_email,draft_data):
    with smtplib.SMTP("smtp.gmail.com",587,timeout=120) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Birthday Wish \n\n {draft_data}")
        print('mail sent')

try:
    data=pandas.read_csv('birthdays.csv')
    new_dict={(data_row['month'],data_row['day']):data_row for (index,data_row) in data.iterrows()}
    print(new_dict)


    name=data.name[(data.month==today_month) & (data.day==today_day)].tolist()[0]
    email=data.email[(data.month==today_month) & (data.day==today_day)].tolist()[0]
    print(name)
    print(email)
except IndexError:
    print(f"Today is not a any birthday, today Date: {now}")
else:
    file_name=random.choice(files)
    print(file_name)
    with open(f'letter_templates/{file_name}','r') as file:
        line=file.read()
    draft=line.replace(PLACEHOLDER,name)
    print(draft)
    send_mail(email,draft)


