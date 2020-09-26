
import smtplib

sender = 'amak4737@gmail.com'
receivers = ['amak4737@gmail.com']

message = """From: From Person <amak4737@gmail.com>
To: To Person <amak4737@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")