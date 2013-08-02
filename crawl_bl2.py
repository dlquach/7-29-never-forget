#!/usr/bin/python

"""""
@author: Derek Quach

Main script for telling the bot to parse the entire front page of r/borderlands2 and search for instances of "shift".

"""""

import urllib2
import re
import emaillib



headers = {'User-Agent' : 'CrawlingBL2/1.0'}
req = urllib2.Request('http://reddit.com/r/borderlands2/')
html = urllib2.urlopen(req).read()

links = re.findall('(?i)http://www.reddit.com/\w*/\w*/comments/\w*/[a-z0-9_]*shift[a-z0-9_]*', html)
print links
print ''

code_array = []

for link in links:
    comment_req = urllib2.Request(link)
    comment_page = urllib2.urlopen(comment_req).read()
    codes = re.findall('(?i)MAC.*?.....-.....-.....-.....-.....', comment_page)

    """ Check if each code has already been sent out or already exists in the code list."""
    for string in codes:
        code = re.findall('.....-.....-.....-.....-.....', string)
        if not code[0] in code_array:
            code_array.append(code[0])

username = ''
password = ''
recipient = ''

with open('emailinfo.txt') as infofile:
    content = infofile.readlines()
    username = content[0]
    password = content[1]
    recipient = content[2]

for code in code_array:
    """ Put the codes into an external file provided that they are not already in the list. """
    with open("shiftcodes.txt", "r+b") as shiftfile:
        if not code in shiftfile.read():
           shiftfile.write('%s\n' % code) 
           print '%s added to the code log.' % code
           emaillib.mail(username, password, recipient, code) 




