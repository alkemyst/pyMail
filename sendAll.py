#!/usr/bin/env python3

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
  try:
    s.send_message(msg)
  except smtplib.SMTPException as e:
    print(e)
  del msg



