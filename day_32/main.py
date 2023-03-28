import smtplib
from secret import email, password, receiver

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=receiver, msg="Subject:test\n\ntest")
