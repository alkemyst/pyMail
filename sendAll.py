import email
import os
import smtplib

smtpPort=25
smtpHost="cernmx.cern.ch"

path = './'
myDir="exampledir/"
listing = os.listdir(myDir)

s = smtplib.SMTP(host=smtpHost, port=smtpPort)

for fle in listing:
  full_path = os.path.join(myDir, fle)
  msg = email.message_from_file(open(full_path))
  s.send_message(msg)
  del msg




