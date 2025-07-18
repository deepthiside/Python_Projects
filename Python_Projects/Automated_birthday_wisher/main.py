import pandas as pd
import datetime as dt
import random
import smtplib

# Your email credentials
MY_EMAIL = "sharadchaturvedi681@gmail.com"
MY_PASSWORD = "ltuxjqcfeannnpom"

# 1. Get today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# 2. Read the birthdays.csv file
data = pd.read_csv("birthdays.csv")

# 3. Create a dictionary with (month, day) as keys
birthdays_dict = {
    (row["month"], row["day"]): row
    for (_, row) in data.iterrows()
}

# 4. Check if today matches any birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]

    # 5. Choose a random letter template
    letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_path) as letter_file:
        contents = letter_file.read()
        personalized_letter = contents.replace("[NAME]", name)

    # 6. Send email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
            )
        print("Birthday email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)
else:
    print("No birthdays today.")
