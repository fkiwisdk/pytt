#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#print('ffffffffffaaa')

#import urllib2   
#import urllib.request
#import re   
#from bs4 import BeautifulSoup  
#from distutils.filelist import findall  

import re,sys
import urllib.request


#page_alllinks = re.findall('<ul id="arcs-list" class="clearfix">(.+?)<div class=\'paging clearfix\'>', news_list_page)

html = urllib.request.urlopen("http://man.linuxde.net/sleep").read().decode('utf-8')
content = re.findall('<div id="arc-body">(.+?)</div><div id="ad-arc-bottom">', html, re.S)
#print(html)
print()
print()
print()
print(content)



