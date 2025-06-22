import smtplib
from email.mime.text import MIMEText

class EmailIntegration:
    def __init__(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password

    def send_email(self, recipient_email, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = recipient_email

        # Use the app password generated above
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(self.sender_email, "nzyz jzzt hloq ztzy")  # Use App Password here
            server.sendmail(self.sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email}!")
