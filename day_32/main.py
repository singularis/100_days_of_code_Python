import smtplib
from secret import email, password, receiver

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs=receiver)