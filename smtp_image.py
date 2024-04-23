import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from stegano import exifHeader


smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "ya.superkesa@gmail.com"
pswd = "bcbsnkqlkgomxeyw"

email_list = ["ya.superkesa@gmail.com", "ya.superkesa@gmail.com", "ya.superkesa@gmail.com"]

subject = "Red panda"

secret = exifHeader.hide("img/3.png", "img/3_secret.png",
                         "Красная панда. Китайцы назвали этого зверя огненной лисой, что звучало как «хон хо». Другим именем было «кошачий медведь». Жители Непала называли это животное «пунья» и именно от этого слова и произошло название «панда».")

def send_emails(email_list):

    for person in email_list:

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        filename = "img/3_secret.png"

        attachment = open(filename, 'rb')

        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filemame= " + filename)
        msg.attach(attachment_package)

        text = msg.as_string()

        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")

        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    TIE_server.quit()

send_emails(email_list)

# result = exifHeader.reveal("~/img/noname.png")
# result = result.decode()
# print(result)
