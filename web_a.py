#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#print('ffffffffffaaa')

#import urllib2   
#import urllib.request
#import re   
#from bs4 import BeautifulSoup  
#from distutils.filelist import findall  

import re
import urllib.request
resp=urllib.request.urlopen("http://man.linuxde.net/mv")

html = resp.read()
html = html.decode('utf-8')
print('------------begin--------')


title = re.findall( '<h1 class="left">(.+?)</h1>', html)


ppp = re.findall('<div class="right"> <a href="(.+?)" rel="tag">(.+?)</a></div>', html)
#for title in zip(title):
#	print(title)

print(title[0])

print(ppp[0][1])

