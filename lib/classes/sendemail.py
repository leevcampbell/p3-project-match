from email.message import EmailMessage
import ssl
import smtplib


def send_email(email_sender, email_password, email_receiver1, email_receiver2):
    body = f"""
    Hey there! You've both matched each other's preferences. Here are your email addresses:
    User 1: {email_receiver1}
    User 2: {email_receiver2}
    Happy matching!
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = [email_receiver1, email_receiver2]
    em['Subject'] = "You've got a match!"
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
send_email('pythontestingphase3@gmail.com','ekzewlnqqveldcri', 'leevcampbell@gmail.com', 'zina.kalu@gmail.com')





