from datetime import datetime
import pandas
import random
import smtplib

my_email = "email@gmail.com"
password = "password"

now = datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday = birthdays_dict[today]
    random_letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(random_letter) as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday["email"],
                            msg=f"Subject:Happy Birthday\n\n{letter}")

