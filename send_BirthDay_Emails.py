
import pandas
import smtplib
from email.message import EmailMessage
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()
gmail = os.getenv("GMAIL")
app_password = os.getenv("APP_PASSWORD")



import random
wishes = [
    "Wishing You a Very Happy Birthday filled with Joy, Success, money whatever You want!",
    "May your birthday be the start of a year full of happiness and dreams come true!",
    "Hope your special day brings you all that your heart desires!"
]

#Read Today's Date:
today = datetime.now().strftime("%d-%m")
print(f"Today's date: {today}")

#Read the CSV file: CSV(Comma separated Values)
readCSV = pandas.read_csv("contacts.csv")
readCSV['DOB'] = readCSV['DOB'].str.replace("/","-", regex=False)

#Check if anyone's birthday is today:
for index, row in readCSV.iterrows():
    if row['DOB'] == today:
        name = row['Name']
        to_email = row['Email']

        #Email Content
        msg = EmailMessage()
        msg['Subject'] = f"🎈Wish You a very Happy Birthday {name}!🍾🎂"
        msg['from'] = gmail
        msg['to'] = to_email
        msg.set_content(f"Dear {name},\n\n{random.choice(wishes)}\n\n - Best Regards, Mustafa (sent via Jarvis🤖)")

        #Send the Email (through Gmail)
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(gmail,app_password)
                smtp.send_message(msg)
                print(f"Birthday wish sent to {name}")

        except Exception as e:
            print(f"❌ Failed to send to {name} : {e}")



