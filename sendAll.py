#!/usr/bin/env python3

import email
import os
import smtplib

smtpPort=25
smtpHost="cernmx.cern.ch"

path = './'
spoolDir="spool/"
sentDir="sent/"

dirMode = 0o700

if (not os.path.exists(spoolDir)) : os.mkdir(spoolDir, dirMode)
if (not os.path.exists(sentDir)) : os.mkdir(sentDir, dirMode)

listing = os.listdir(spoolDir)

s = smtplib.SMTP(host=smtpHost, port=smtpPort)

for emlFile in listing:
  spool_path = os.path.join(spoolDir, emlFile)
  sent_path = os.path.join(sentDir, emlFile)
  msg = email.message_from_file(open(spool_path))
  try:
    s.send_message(msg)
  except smtplib.SMTPException as e:
    print(e)
  del msg
  os.replace(spool_path, sent_path)



