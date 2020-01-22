# Import lib for sending emails with SMTP
import smtplib

class Email():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send_email(self, receiver_email, stock_ticker, price):
        """
        Sends an email to a specificed recevier\n
        Params:
        `receiver_email`(string) -> The receiver email that the email should be sent to
        """
        email_text = "From: {sender}\nTo: {to}\nSubject: Price alert triggered for {stock}\n\nOne of the stocks you were tracking has triggered a price alert. {stock} has just crossed your price alert of {price}."
        email_text = email_text.format(sender="Price Alerts", to=receiver_email, stock=stock_ticker, price=price)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(self.username, self.password)
        server.sendmail(self.username, receiver_email, email_text)
        server.close()
