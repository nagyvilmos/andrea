import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
import markdown
# creates SMTP session
with smtplib.SMTP('smtp.gmail.com', 587) as s:
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("william.norman.walker@gmail.com", "uygb eslv qsep jjsq")
    # message to be sent
    msg = EmailMessage()


    text = "## An email!\n\nAn email! From **the** computer!\n\nInnit smart?"

    msg['To'] = Address("William", "william.norman.walker", "gmail.com")
    msg['From'] = Address("The System", "noreply", "wibble.com")
    msg['Subject'] = "A test Message from the system"
    msg.set_content(text)

    msg.add_alternative(f"""\
    <html>
    <head></head>
    <body>{markdown.markdown(text)}
    </body>
    </html>
    """.format(), subtype='html')
    # note that we needed to peel the <> off the msgid for use in the html.
    # sending the mail
    s.send_message(msg)
