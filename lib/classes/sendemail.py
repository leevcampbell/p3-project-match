from email.message import EmailMessage
import ssl
import smtplib
from lib.classes.users import User

current_user = User.grab_current_user()
match_users = User.query_for_match()



def send_email(email_sender, email_password, match_users, current_user):
    body = f"""
    Hey there! You've both matched each other's preferences. Here are your email addresses:
    User 1: {current_user.email}
    User 2: {match_users.email}
    Happy matching!
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = [current_user.email, match_users.email]
    em['Subject'] = "You've got a match!"
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)

    send_email('pythontestingphase3@gmail.com', "ekzewlnqqveldcri", f"{match_users.email}", f'{current_user.email}')





