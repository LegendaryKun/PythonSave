#亚马逊图书信息获取


import requests
from bs4 import BeautifulSoup
import re

GetUsers_url = 'https://www.amazon.cn/dp/B001BKVXOA/ref\
=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords\
=Core+Python+Applications+Programming&qid=1553266952&s=gateway&sr=8-1'
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'}

#html = requests.get(GetUsers_url,headers = headers)
html = requests.get(GetUsers_url)
html = BeautifulSoup(html.text, 'html.parser')


bookname = html.find('span',class_="a-size-large").text
print('您所查找的亚马逊图书：《%s》\n'%(bookname))


soup = html.find_all('noscript')
soup = re.findall('<div>.+?<br/>',str(soup))
soup = re.split('<div> |<br/>',soup[0])
soup.pop(0)
soup.pop(-1)
print('《%s》简介：'% bookname)
print(soup)


soup = html.find('div',class_="content")
soup.style.clear()
print('\n《%s》基本信息：'%bookname)
for infor in soup.find_all('li'):
           print(re.findall('(?m)\w{1}.+',infor.text))




