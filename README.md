# Birthday Email Bot 🎂📧

This is a simple Python project I made that automatically sends birthday emails to people on their special day.

## 💡 What it does

- Reads birthday details (name, email, date) from a CSV file
- Checks if today is someone's birthday
- If yes, it sends them a birthday email using your Gmail account

## 🧠 Tech Used

- **Python**
- **pandas** – for handling CSV data
- **smtplib** and **email.message** – to send emails
- **schedule** – for running the bot every day
- **datetime** – to check the date

## 🔧 How to Use

1. Clone this repo to your system

```bash
git clone https://github.com/YourUsername/Birthday_Email_Bot.git
cd Birthday_Email_Bot

Make sure you have Python installed (version 3.10 or above).

Install the needed libraries:

pip install -r requirements.txt
Add your Gmail and password in the code (you can also use an App Password for security).

Add a CSV file like this:

name,email,day,month
Ali,ali@example.com,18-7
Sara,sara@example.com,25-12
Run the bot:

python birthday_bot.py
or if you're using schedule, just let it run in background.

📦 Files
birthday_bot.py – main logic of the bot

birthdays.csv – data file for storing birthday info

requirements.txt – all libraries needed

❗Important Notes
Your Gmail must allow less secure apps or use an App Password

Make sure to test it with your own email before using on others

