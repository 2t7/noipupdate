#!/usr/bin/env python
"""
Script for updating all noip-hosts over the web-login.
mayor parts adapted from http://stackoverflow.com/questions/4720470/using-python-and-mechanize-to-submit-form-data-and-authenticate
This script also uses bs4, but only for isolating the sucess messages (->could be removed if bs4 not available)
Promising additional resource for browser emulation: http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/
IMPORTANT:
Make sure that this file can not be read by unauthorized people since it will contain username and password of your noip-account.
You might want to store the file on an encrypted partition/home directory

Copyright 2014 martin@2t7.de

GNU GENERAL PUBLIC LICENSE
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import mechanize
import bs4

br = mechanize.Browser()
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.addheaders=[("User-agent","Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0")] #some Win7 IE10.6 user-agent
r= br.open('https://noip.com/login')

br.select_form(nr=0)
br.form['username'] = ''  #username goes here
br.form['password'] = ''  #password goes here
br.submit()
br.open("https://www.noip.com/members/dns")
linklist=list()
for link in br.links():
  if link.text=="Modify":
    linklist.append(link.url)
for url in linklist:
  br.open(url)
  br.select_form(nr=0)
  response=br.submit()
  soup=bs4.BeautifulSoup(response.read())         #------------------
  found= soup.find(attrs={"class":"successbox"})  #Remove this if bs4
  if found!=None:                                 #is not available
    print found.p.getText()                       #or if you trust
  else:                                           #the script to work
    exit(1)                                       #------------------
exit(0)
