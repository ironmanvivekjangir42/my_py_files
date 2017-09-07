#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.login('username','password')
s.sendmail('from','to','msg')
s.close()