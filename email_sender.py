import smtplib

# Allow to create SMTP server which is communicating. This is an BUILTIN feature in Python!
from email.message import EmailMessage
# https://docs.python.org/3/library/string.html#string.Template.template
from string import Template
# For read the index.html we need one other modul, convert it to template and substitute it:
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'John Doe'
email['to'] = 'Your test email@protonmail.com'
email['subject'] = 'You will earn 1,000,000 Eur soon!'

email.set_content(html.substitute({'name': 'Jupiter'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # TLS is an encryption mechanism to connect securely to the server.
    smtp.login('Your dev email@gmail.com', 'xxxx xxxx xxxx xxxx')  # https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
    smtp.send_message(email)
    print('all good BB!')
    