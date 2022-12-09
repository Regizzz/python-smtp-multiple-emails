import smtplib
import ssl
import csv
import time

port = 465
smtp_server = "smtp_server_address_here"
sender = "your_email_here"
sender_password = "password_here"

SSL_context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=SSL_context) as server:
    server.login(sender, sender_password)
    with open("sample.csv", newline='') as file_handle:
        reader = csv.reader(file_handle, delimiter=' ')
        for row in reader:
            server.sendmail(sender, row[0], row[1]+' '+row[2])
            time.sleep(1)

