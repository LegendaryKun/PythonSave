#在凡科建站上创建网页添加学号，然后读取学号
'''
当在网页上修改学号时，可能改变网页的HTML导致获取学号信息错误
，这时可以把当前文本删除，然后新建文本重新添加学号。
'''

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
soup = html.find_all('noscript')
soup = re.findall('<div>.+?<br/>',str(soup))
soup = re.split('<div> |<br/>',soup[0])
soup.pop(0)
soup.pop(-1)
print(soup)


#print(html)
#soup = html.find('div',class_="fk-editor simpleText fk-editor-break-word ")
#print(soup)
#print(soup.text)

#soup = soup.find_all('div')

#soup = html.find_all('noscript')
#print(soup[1])

#print(soup)
'''
L = []
for i in soup:
           i = str(i)
           i = i.strip('</div>')
           L.append(i)
           
print(L)

'''



