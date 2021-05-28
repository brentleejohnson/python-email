import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# please note go to https://myaccount.google.com/lesssecureapps and
# turn it off to allow gmail to send
# creates SMTP session

sender_email_id = "brentleejohnson73@gmail.com"
receiver_email_id = ["naeemahndavis@gmail.com", "jasoncee017@gmail.com", "thapelo@lifechoices.co.za"]
password = input("Password: ")
Subject = "Testrun"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ", ".join(receiver_email_id)
msg['Subject'] = Subject
body = "Hey\n"
body = body + "Testing my coding for an email"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# authentication
s.login(sender_email_id, password)

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)

# s.sendmail(sender_email_id, receiver_email_id, text)

# terminating the session
s.quit()
