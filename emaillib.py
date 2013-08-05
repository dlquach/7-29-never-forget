#!/usr/bin/python

"""""
@author: Derek Quach

Emailing functions. Requires username and password to a gmail account to use properly.

"""""

"""
The Subject line will always state that the message contains a code and the body should include the URL to the comments section used.
"""
def mail(sender_name, sender_pass, receiver, code, url):
    import smtplib
    import datetime

    """ Get the time of day so we can timestamp our emails. """
    now = datetime.datetime.now()

    try:
        s = smtplib.SMTP()
        s.connect('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_name, sender_pass)
        body = 'Mac/PC Code: %s\nFound at: %s' % (code, url)
        full_message = 'Subject: %s\n\n%s' % ("Shift Codes for %s" % now.strftime('%Y-%m-%d at %H:%M'), body)
        s.sendmail(sender_name, receiver, full_message)
        print 'Sent message!'
    except Exception,R:
        print R
