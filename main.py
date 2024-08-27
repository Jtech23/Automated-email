import smtplib
import os

sender_email = os.getenv("MY_EMAIL")
sender_password = os.getenv("PASSWORD")
receiver_email = "jerrykolade04@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    try:
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,  # Use recipient's email from data
                            msg="SUBJECT:GREETING\n\nHello world!")
        print(f"Email sent successfully to {name}")
    except (smtplib.SMTPConnectError, smtplib.SMTPAuthenticationError) as e:
        print(f"Error sending email: {e}")

