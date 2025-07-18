import schedule
import time
import random
import pandas
import smtplib
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
gmail = os.getenv("GMAIL")
password = os.getenv("PASSWORD")

wishes = [
    "Wishing You a Very Happy Birthday filled with Joy, Success, money whatever You want!",
    "May your birthday be the start of a year full of happiness and dreams come true!",
    "Hope your special day brings you all that your heart desires!"
]



def send_birthday_emails():
    print("Checking Birthdays...")
    today = datetime.now().strftime("%d/%m")
    csvFile = pandas.read_csv("contacts.csv")
    csvFile['DOB'] = csvFile['DOB'].str.replace("-","/", regex=False)

    birthday_found = False

    for index, row in csvFile.iterrows():
        if row['DOB'] == today:
            to = row['Email']
            name = row['Name']
            subject = "Happy Birthday!"
            message = f"Dear {name}! {random.choice(wishes)} - Best Wishes, Mustafa (sent via Jarvis) "
            birthday_found = True

            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(gmail, password)
                    smtp.sendmail(from_addr=gmail, to_addrs=to, msg=f"Subject: {subject}\n\n{message}")

                print(f"Birthday mail sent to {name}")

            except Exception as e:
                print(f"Failed to send Birthday mail to {name} : {e}")

    if not birthday_found:
        print("No Birthdays found")


# schedule.every().day.at("10:20").do(send_birthday_emails)
schedule.every(5).seconds.do(send_birthday_emails)

print("Birthday Bot Running...")

while True:
    schedule.run_pending()
    time.sleep(1)
