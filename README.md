# Automated Email Sender

This project demonstrates how to automate email sending using Python.

## Required Modules

- `smtplib`: Allows creating and communicating with an SMTP server. This is a built-in feature in Python.
- `email.message.EmailMessage`: To create the email message.
- `string.Template`: To handle email templates.
- `pathlib.Path`: To read the index.html file and convert it to a template.

## Usage

This project does not include the customer database!

## Running

To run the script, use the following command in the terminal:
python3 email_sender.py

## Notes
To use the SMTP server, ensure that the smtplib.SMTP host and port are set correctly.
For the smtp.login section, you need to provide your own email address and password. Please be cautious with handling sensitive information.
Google no longer supports less secure apps. For more information, visit: Stack Overflow - [Sending email with Python Google disables less secure apps.](https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps)
