import smtplib
import keyring
from os import system
from email.message import EmailMessage
from creds import EMAIL_ID, EMAIL_PASS

try:
    system("cls")
    
    msg = EmailMessage()
    with smtplib.SMTP("outlook.office365.com", 25) as smtp:
        print(smtp.ehlo())
        smtp.starttls()
        smtp.login(EMAIL_ID, EMAIL_PASS)
        print("login successful")

        msg["From"] = EMAIL_ID
        msg["To"] = EMAIL_ID
        msg["Subject"] = "Automated Email using smtp-lib"
        msg.set_content("This is a automated demo email using smtplib")

        print(smtp.send_message(msg))

except Exception as ex:
    print(f"Config Error : {ex.args}")