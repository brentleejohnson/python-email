import smtplib
# please note go to https://myaccount.google.com/lesssecureapps and
# turn it off to allow gmail to send
# creates SMTP session
s = smtplib.SMTP("smtp.gmail.com", 587)
sender_email_id = "brentleejohnson73@gmail.com"
receiver_email_id = "naeemahndavis@gmail.com"
password = input("Enter senders email password: ")
# start TLS for security
s.starttls()
# authentication
s.login(sender_email_id, password)
# sending the mail
message = "Greetings\n"
message = message + "Testing email coding"
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()
