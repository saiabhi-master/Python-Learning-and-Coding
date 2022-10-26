import random
import smtplib
#
my_email = "testingtester3690@gmail.com" #part before @sign is the identity of my emailaccount
#after @ => identity of email provider
password = "gidv heet lqys kdss"
#
#



import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()



# date_of_birth = dt.datetime(year=2005, month=7, day=7)

if day_of_week == 3:
    with open("quotes.txt", mode="r") as file:
        total_lines = file.readlines()
        random_line = random.choice(total_lines)
        print(random_line)

    with (smtplib.SMTP("smtp.gmail.com", port=587)) as connection: #establishing connection
        connection.starttls()
        #way of securing connection to email server
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="testingtester3690@yahoo.com",
                            msg=f"Subject:Hello\n\n{random_line}")



