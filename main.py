##################### Hard Starting Project ######################
import datetime as dt
import readline
import smtplib
import pandas
import random

today = dt.datetime.now()
today_tuple = (today.month, today.day)

df = pandas.read_csv("../bday-wisher-project/birthdays.csv")
# print(bday_data["month"])
birthdays_dict = {
    (data["month"], data["day"]) : data for (index, data) in df.iterrows()
}

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

if today_tuple in birthdays_dict:
    letter_name = random.choice(letters)
    with open(f"letter_templates/{letter_name}", "r") as letter:
        letterdata = letter.read()
        letterdata = letterdata.replace("[NAME]", birthdays_dict[today_tuple]["name"])
    my_email = "youremail@gmail.com"
    password = "yourpassword"
    target_mail = birthdays_dict[today_tuple]["email"]
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  #make conn secure!
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=target_mail, msg=f"Subject:Happy Birthday\n\n{letterdata}")


