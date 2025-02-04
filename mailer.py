import smtplib
from settings import Settings
import random

class GoodMorningMailer:
    def __init__(self):
        self.settings = Settings()
        self.email = self.settings.EMAIL
        self.password = self.settings.PASSWORD
        self.recipients = ["jairellezoldyck@gmail.com", "antipasado2004@gmail.com", "acegabriel0710@gmail.com"]

    def connect(self):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(self.email, self.password)
        return connection

    def send_mail(self, subject, message):
        with self.connect() as connection:
            email_content = f"Subject:{subject}\n\n{message}".encode("utf-8")
            connection.sendmail(self.email, self.recipients, email_content)
            print("Email Sent")

    def get_random_quote(self):
        with open("data/quote.txt", encoding="utf8") as file:
            quotes = file.readlines()

        return random.choice(quotes)

    def get_email_body(self):
        with open("data/message.txt", encoding="utf8") as file:
            body = file.read()
            body.replace("[QUOTE]", self.get_random_quote())

        return