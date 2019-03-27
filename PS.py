#亚马逊图书信息获取
#在亚马逊上搜索任意一本图书，在基本信息栏找到ASIN，运行脚本输入ASIN，即可获取图书信息

import requests
from bs4 import BeautifulSoup
import re


ASIN = input('请输入亚马逊图书ASIN编号：')  #亚马逊每本图书都有自己的ASIN，通过ASIN即可获取指定图书信息
GetUsers_url = 'https://www.amazon.cn/dp/'+ASIN
html = requests.get(GetUsers_url)
html = BeautifulSoup(html.text, 'html.parser')


bookname = html.find('span',class_="a-size-large").text    #获取图书名
print('您所查找的亚马逊图书：《%s》\n'%(bookname))


soup = html.find_all('noscript')              #获取图书简介
for intro in soup:
           intro = intro.find('div')  #noscript标签有多个，这里寻找含有div的标签
           if intro:
                      print('《%s》简介：'% bookname)
                      intro = re.split('海报：',intro.text) #简介中去除‘海报：’（有的图书提取的简介信息含有多余‘海报：’）
                      print(intro[0])                       #有的简介结尾处不含‘海报：’，这里直接选择list中首元素即可。


soup = html.find('div',class_="content")    #获取图书基本信息
soup.style.clear()                          #style标签中含无用信息
print('\n《%s》基本信息：'%bookname)
for infor in soup.find_all('li'):
           print(re.findall('(?m)\w{1}.+',infor.text))




