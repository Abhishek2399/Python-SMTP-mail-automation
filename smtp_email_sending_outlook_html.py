import smtplib # contains the smtp methods for communicating with server and sending emails
from os import system 
from creds import EMAIL_ID, EMAIL_PASS # importing the email_id and password
from email.message import EmailMessage # for creating the message object

try:
    system("cls")
    # we need an email message object to pack all the information of a mail in a single object
    msg = EmailMessage()
    # using the SMTP method to establish connection with the outlook server
    # port used for comminication is 587 which is a startTLS port 
    # startTLS means it will start a tls communication when asked to else it will do plain communication
    with smtplib.SMTP("outlook.office365.com", 25) as smtp:
        # starting the TLS
        smtp.starttls()
        # ehlo helps us to check the establish connection
        print(smtp.ehlo())
        # not using the email id and password directly for security purpose
        # they are imported from creds.py module
        if EMAIL_PASS != None and EMAIL_ID != None:
            # logging in the outlook mail
            smtp.login(EMAIL_ID, EMAIL_PASS)
            msg["From"] = EMAIL_ID # sender of the email
            msg["To"] = EMAIL_ID # receiver of the email, incase multiple receivers use CSV string where each value is an email
            msg["Subject"] = "Automated HTML Embeded Email test" # subject of the email
            # mentioned below method is used to embed the html type data in the mail body, hence the subtype is "html"
            msg.add_alternative("""
            <html>
                <body>
                    <h1 style="color: bisque;">HTML Embeded Demo</h1>
                </body>
            </html>
            """, subtype="html")
            # sending the msg-object all together
            smtp.send_message(msg)
            print("Sent Successfully")
        else:
            raise Exception(f"Re-check Email : {EMAIL_ID} and Password : {EMAIL_PASS}")
except Exception as ex:
    print(f"Config Error : {ex.args}")