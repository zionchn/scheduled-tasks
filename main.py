import pandas as pd
import smtplib
import datetime as dt
import random

##################### Extra Hard Starting Project ######################
my_email = "nzubechukwunelo@gmail.com"
password = "cerkosdywnbatycq"

# 1. Update the birthdays.csv
b_day = pd.read_csv("birthdays.csv")


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
birth_month = now.month
birth_day = now.day

for _, row in b_day.iterrows():
    if birth_month == row["month"] and birth_day == row["day"]:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        wishes = [f"letter_templates/letter_{random.randint(1,3)}.txt"]
        random_file = random.choice(wishes)

        with open(random_file) as data:
            contents = data.read()
            contents = contents.replace("[NAME]", row["name"])
            random_wishes = random.choice(contents)
            print(contents)


# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr="nzubechukwunelo@gmail.com",
                to_addrs=row["email"],
                msg=f"Subject: Happy Birthday!\n\n{contents}"
            )




