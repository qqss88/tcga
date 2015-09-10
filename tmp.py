#!/usr/bin/env python

import smtplib

gmail_user = 'qqss88@gmail.com'
gmail_pwd = "2009/Erin"
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_pwd)

def send_email(uzr, mail_addr, body):
        smtpserver.sendmail(uzr, mail_addr, body)


file_in = open('project_input.txt')
all_lines = file_in.readlines()
file_in.close()

for line in all_lines:
    person = line
    cleaned = person.split(",")
    name = cleaned[0].strip()
    print name
    email = cleaned[1]
    print email
    score1 = cleaned[2]
    print score1
    score2 = cleaned[3]
    print score2
    score3 = cleaned[4]
    print 'score3 is:', score3
    total_score = str(int(score1) + int(score2) + int(score3))
    email_body = "Hi,"+name+","+"your total score is"+total_score
    send_email(gmail_user, email, email_body)
print 'done.'    
