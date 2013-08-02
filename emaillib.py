#!/usr/bin/python

"""""
@author: Derek Quach

Emailing functions. Requires username and password to a gmail account to use properly.

"""""

def mail(sender_name, sender_pass, receiver, Message):
    import smtplib
    try:
        s = smtplib.SMTP()
        s.connect('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_name, sender_pass)
        s.sendmail(sender_name, receiver, Message)
        print 'Sent message!'
    except Exception,R:
        print R

def test():
    print 'hello world'
