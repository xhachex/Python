import smtplib

gmail_user = "email@gmail.com"
gmail_password = "password"

sender = gmail_user
receiver = "mail"
message = """\
Subject: Hi

This message is sent from Python."""

try:
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(sender, receiver, message)
	print ("Login success")
except:
	print ("Error...")
