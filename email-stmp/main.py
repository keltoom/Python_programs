import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day = now.weekday()

with open("quotes.txt", encoding='utf8') as file:
    data = file.readlines()
    quote = random.choice(data)
    #print(quote)

# HOST
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com



my_email = "email@gmail.com"
password = "password"
if day == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="email@yahoo.com",
                            msg=f"Subject:Saturday Motivation\n\n{quote}".encode('utf-8'))
