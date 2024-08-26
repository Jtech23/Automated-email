import smtplib
import os

sender_email = os.getenv("MY_EMAIL")
sender_password = os.getenv("PASSWORD")
receiver_email = "jerrykolade04@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=sender_email, password=sender_password)
    connection.sendmail(from_addr=sender_email,
                        to_addrs=receiver_email,
                        msg="SUBJECT:GREETING\n\nHello world!")
