import pandas as pd
import smtplib
from twilio.rest import Client

# Twilio Config (Replace with your credentials)
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE = "+1234567890"
USER_PHONE = "+9876543210"

# Email Config
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"

def send_sms_alert(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=USER_PHONE
    )
    print("📱 SMS Alert Sent!")

def send_email_alert(message):
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, f"Subject: Energy Alert!\n\n{message}")
    server.quit()
    print("📧 Email Alert Sent!")

def check_anomalies():
    df = pd.read_csv("data/anomaly_detected.csv").tail(1)
    if df.iloc[0]['Anomaly'] == -1:
        message = f"⚠️ Alert! Unusual energy consumption detected at {df.iloc[0]['Timestamp']}!"
        send_sms_alert(message)
        send_email_alert(message)

if __name__ == "__main__":
    check_anomalies()
