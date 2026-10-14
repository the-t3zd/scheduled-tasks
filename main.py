import pandas
import random
import datetime as dt
import smtplib

MY_EMAIL = "123"
SMTP_SERVER = "smtp.gmail.com"
MY_PASSWORD = "123"

def send_wishes(pandas_series):
    name = pandas_series["name"]
    email = pandas_series["email"]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as template:
        letter = template.read()
        personalized_letter = letter.replace("[NAME]", name)
    email_text = f"Subject:Happy birthday {name}!\n\n{personalized_letter}"
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=email_text
        )
        print(f"Email to {name} sent successfully")


now = dt.datetime.now()
current_date = now.day
current_month = now.month

list_of_people_df = pandas.read_csv("birthdays.csv")

for index, row in list_of_people_df.iterrows():
    if row.month == current_month and row.day == current_date:
        print("target found")
        current_entry = row
        send_wishes(current_entry)
    else:
        print("Not found")
