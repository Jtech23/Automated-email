import smtplib
import pandas
import os

sender_email = os.getenv("MY_EMAIL")
sender_password = os.getenv("PASSWORD")
receiver_email = "jerrykolade04@gmail.com"

data = pandas.read_csv("birthdays.csv")
details = {(row.name, row.email): row for (index, row) in data.iterrows()}

for (key, value) in details.items():
    name = value["name"]

    with open(f"letter_templates/Jerry.txt", "r") as text:
        final_let = text.read()
        final_letter = final_let.replace("[NAME]", name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        try:
            connection.login(user=sender_email, password=sender_password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=f"subject:INVITATION TO AGRICULTURE DRONE SHOW 2024\n\n{final_letter}")
            print(f"Email sent successfully to {name}")
        except (smtplib.SMTPConnectError, smtplib.SMTPAuthenticationError) as e:
            print(f"Error sending email: {e}")
