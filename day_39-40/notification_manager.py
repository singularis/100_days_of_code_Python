import smtplib

class NotificationManager:
    def __init__(self, email, password):
        print("create channel")
        self.email = email
        self.password = password

    def send_notification(self, receiver: str, city: str, price: str) -> None:
        print("Sending")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email, to_addrs=receiver, msg=f"Subject: Price for {city} goes lower "
                                                                             f"Check data for {city}, now it is {price}")
