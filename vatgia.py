#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import requests
from bs4 import BeautifulSoup

os.system('cls')
time.sleep(1)
print '\n>> THU THAP DU LIEU WEBSITE VATGIA.COM << \n'
time.sleep(1)
def vatgia():
    page = 0
    myString = 'http://www.vatgia.com/2741/giay-the-thao.html,'
    name = raw_input(str('\nNhap ten tep muon luu : '))
    time.sleep(1)

    while page<50:
          page = page + 1
          url = myString+str(page)
          print '\nDang tien hanh thu thap du lieu trang thu',page
          r = requests.get(url)
          thongtin = BeautifulSoup(r.content,'html.parser')
          data = thongtin.find_all("div", {"class":"block no_picture_thumb"})
          filename = name+'.txt'
          f = open(filename,"a")

          for item in data:
               ten = item.find_all("div", {"class":"name"})[0].text
               chitiet = item.find_all("div", {"class": "more_content"})[0].text
               gia = item.find_all("div", {"class":"price"})[0].text
               diadiem = item.find_all("div", {"class":"estore"})[0].text
               capnhat = item.find_all("span", {"class":"last_update"})[0].text

               f.write('Tên sản phẩm :' +'\t\t' + ten.encode('utf-8')+ "\n")
               f.write('Chi tiết sản phẩm :' +'\t\t' + chitiet.encode('utf-8')+ "\n")
               f.write('Gía tiền :' +'\t\t\t' + gia.encode('utf-8')+ "\n")
               f.write('Nơi bán :' +'\t\t\t'+diadiem.encode('utf-8')+ "\n")
               f.write('Thời gian cập nhật :' +'\t' + capnhat.encode('utf-8') + "\n")
               f.write('\n')
          f.close()

    print '\nHoan thanh !!!'
    time.sleep(1)
    print '\nMoi ban mo tep '+  name + ' dinh kem ! '
    time.sleep(1)
    print '\nversion 2.1 code by nguyendactoan'
vatgia()


     


       
    


     

