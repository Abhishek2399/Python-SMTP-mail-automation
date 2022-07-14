import smtplib
from os import name, system, path
from creds import EMAIL_ID, EMAIL_PASS
from email.message import EmailMessage
from pathlib import Path

try:
    system("cls")
    msg = EmailMessage()
    host = "outlook.office365.com"
    port = 25
    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        print(smtp.ehlo())
        smtp.login(EMAIL_ID, EMAIL_PASS)

        msg["From"] = EMAIL_ID
        msg["To"] = EMAIL_ID
        msg["subject"] = "Autmated test email with attachment"

        # attaching image type attachment
        try:
            with open(path.abspath("Demo_img.jpg"), 'rb') as attachment:
                attachment_name = Path(attachment.name).name
                attachment_data = attachment.read()
            msg.add_attachment(attachment_data, maintype="application", subtype="octet-stream", filename=attachment_name)
        except Exception as ex:
            print(f"Attachment Error : {ex.args}")

        # attaching pdf type attachment
        try:
            with open(path.abspath("pywin32.pdf"), "rb") as attachment:
                attachment_name = Path(attachment.name).name
                attachment_data = attachment.read()
            msg.add_attachment(attachment_data, maintype="application", subtype ="octet-stream", filename=attachment_name)
        except Exception as ex:
            print(f"PDF Attachment Error : {ex.args}")

        smtp.send_message(msg)
        print("Sent Successfuly")
        
except Exception as ex:
    print(f"Config Error : {ex.args}")


