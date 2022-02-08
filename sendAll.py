#!/usr/bin/env python3

import email
import os
import smtplib
from datetime import datetime

smtpPort=25
smtpHost="cernmx.cern.ch"

path = './'
spoolDir="Spool/"
sentDir="Sent/"
logFile="log.txt"

dirMode = 0o700

if (not os.path.exists(spoolDir)) : os.mkdir(spoolDir, dirMode)
if (not os.path.exists(sentDir)) : os.mkdir(sentDir, dirMode)

dateTimeObj = datetime.now()
myLog = open(logFile, 'a+')
myLog.write("Send invoked at " + dateTimeObj.strftime("%Y-%b-%d %H:%M:%S") + " : " );

listing = os.listdir(spoolDir)
s = smtplib.SMTP(host=smtpHost, port=smtpPort)

nMail=0

for emlFile in listing:
  spool_path = os.path.join(spoolDir, emlFile)
  sent_path = os.path.join(sentDir, emlFile)
  msg = email.message_from_file(open(spool_path))
  try:
    s.send_message(msg)
  except smtplib.SMTPException as e:
    print(e)
  del msg
  nMail=nMail+1
  os.replace(spool_path, sent_path)



myLog.write("%d email(s) sent\n" % nMail);
myLog.close()
