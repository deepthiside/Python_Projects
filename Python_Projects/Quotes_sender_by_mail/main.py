# ltux jqcf eann npom
# import smtplib
#
my_email = "sharadchaturvedi681@gmail.com"
password = "ltuxjqcfeannnpom"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user = my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="jaintanisha066@gmail.com",
#         msg="Subject: Hello cutieeee \n\n I am so happy with youuu."
#     )
# import datetime as dt
# from calendar import month
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2005,month=10,day=16)
# print(date_of_birth)
import smtplib
import random
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jaintanisha066@gmail.com",
            msg=f"Subject: Tuesday Motivation  \n\n {quote}"
        )




