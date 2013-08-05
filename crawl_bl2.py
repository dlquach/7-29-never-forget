#!/usr/bin/python

"""""
@author: Derek Quach

Script for telling the bot to parse the entire front page of r/borderlands2 and search for instances of "shift".

How it works:
    The front page of r/borderlands2 is requested and scanned for all of its links to comments (since codes are
    typically posted in the comments section). Only links to threads that have the word shift in the title are
    actually grabbed. Each of these topics then have their comments scanned for content matching the pattern for a
    shift code. Since Mac and PC codes are typically presented together, the keyword we search for is Mac instead of
    PC (pc is used a lot in HTML code).

    This crawler must be accompanied by a text file called shiftcodes.txt and an email info file called emailinfo.txt.
    Codes will be stored in the aforementioned text file to be able to check against sending the same code twice.

    Shift codes are of the form xxxxx-xxxxx-xxxxx-xxxxx-xxxx.

"""""

import urllib2
import re
import emaillib


""" Trying to get around the fact that Reddit heavily rate limits requests by urllib2 """
headers = {'User-Agent' : 'CrawlingBL2/1.0'}
req = urllib2.Request('http://reddit.com/r/borderlands2/')
html = urllib2.urlopen(req).read()

""" Regex to find all URLs to the comments of each post that also has 'shift' (case insensitive) in the title. """
links = re.findall('(?i)http://www.reddit.com/\w*/\w*/comments/\w*/[a-z0-9_]*shift[a-z0-9_]*', html)
print links
print ''

code_array = []

for link in links:
    comment_req = urllib2.Request(link)
    comment_page = urllib2.urlopen(comment_req).read()
    """  I'm particularly interested in PC codes but using Mac as the pattern to match ensures we don't get random HTML code in the results. """
    codes = re.findall('(?i)MAC|PC.*?.....-.....-.....-.....-.....', comment_page) 

    """ Check if each code has already been sent out or already exists in the code list. """
    for string in codes:
        code = re.findall('.....-.....-.....-.....-.....', string)
        if not code:
            break
        if not code[0] in code_array:
            code_array.append([code[0], link])

username = ''
password = ''
recipient = ''

""" Grab the email info. """
with open('emailinfo.txt') as infofile:
    content = infofile.readlines()
    username = content[0]
    password = content[1]
    recipient = content[2]

new_codes_found = 0

for code in code_array:
    """ Put the codes into an external file provided that they are not already in the list. """
    with open("shiftcodes.txt", "r+b") as shiftfile:
        if not code[0] in shiftfile.read():
            shiftfile.write('%s\n' % code[0]) 
            print '%s added to the code log.' % code[0]
            emaillib.mail(username, password, recipient, code[0], code[1]) 
            new_codes_found = new_codes_found + 1

if new_codes_found == 0:
    print 'No new codes at this time.'
else:
    print '%d new codes found and submitted.' % (new_codes_found) 

