# -*- encoding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
from urllib2 import urlopen

def khaithac_dulieu(url):
    w=urllib.urlopen(url)
    return BeautifulSoup(w,'html.parser')
i=1
print ('\n\tAUTO DOWNLOAD IMAGES USE PYTHON -version 1.0')
dulieu = khaithac_dulieu(str(raw_input('\nEnter the url: ')))
print '\nStart Download Images.....'
for img in dulieu.find_all('img'):
    temp = img.get('src')
    if temp[:1] == '/':
        image = 'dulieu' + temp
    else:
        image = temp
    
    nametemp = img.get('alt')
    filename = str(i)
    i=i+1
    imagefile = open(filename + '.jpeg','wb')
    imagefile.write(urllib.urlopen(image).read())
    imagefile.close()
    print(img.get('src'))
print '\nSave images !'  
    


