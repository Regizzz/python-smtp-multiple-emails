<div align="center">

# python-smtp-multiple-emails

</div>

This script is for sending emails to multiple recipents. 

## Usage

Replace `smtp_server_address_here` to your smtp-server address in `smtpshit.py` file
```smtp_server = "smtp_server_address_here"````

Replace `your_email_here` to your  sender-email address in `smtpshit.py` file
```sender = "your_email_here"```

Replace `password_here` to your  sender-email address in `smtpshit.py` file
```sender_password = "password_here"```

Fill `sample.csv` file with your emails and messages like in example
```test@example.com username password```

Run the script
```python smtpshit.py```

Script takes first column as a email address then sends a message which is made up from second and third columns.
```message = "username password"```

Recipent will recieve email like this
```username password```
