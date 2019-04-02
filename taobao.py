#Selinium 登录淘宝
#还需加上截取显示验证码
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import datetime

class taobao_infos:

    def __init__(self,url,buytime):
        #self.url = 'https://login.taobao.com/member/login.jhtml'  #淘宝登录页面
        self.url = url
        self.buytime = buytime
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()  #这句我加进去的
        self.wait = WebDriverWait(self.browser, 10)

    #处理登陆信息
    def login(self):
        self.browser.get(self.url)
        sleep(6)
        self.browser.find_element_by_xpath('//*[@class="forget-pwd J_Quick2Static"]').click() #密码登录
        sleep(2)
        self.browser.find_element_by_xpath('//*[@class="weibo-login"]').click()    #微博登录
        sleep(3)
        self.browser.find_element_by_name('username').send_keys('17865570232')  
        sleep(5)
        self.browser.find_element_by_name('password').click() #这一步是我加上去的，我发现登录时模仿鼠标点击输入框，验证码才会显示
        sleep(3)
        self.browser.find_element_by_name('password').send_keys('wb1324')
        sleep(4)
        Vcode = input('请输入验证码：')
        self.browser.find_element_by_name('verifycode').send_keys(Vcode)
        sleep(4)        
        self.browser.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()  #登录        
        sleep(8)

    #结算
    def settle(self):  
        self.browser.get("https://cart.taobao.com/cart.htm")     #购物车
        self.browser.find_element_by_id("J_SelectAll1").click()  #全选
        sleep(1)
        self.browser.find_element_by_link_text("结 算").click();
        now = datetime.datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S')) #格式化datetime

    def buy_on_time(self):
             while True:
               now = datetime.datetime.now()
               if now.strftime('%Y-%m-%d %H:%M:%S') == self.buytime:
                 while True:
                   try:
                     print(datetime.datetime.now())
                     driver.find_element_by_link_text('提交订单').click()
                   except:
                     sleep(1)
               sleep(0.1)


url = 'https://login.taobao.com/member/login.jhtml'   #淘宝登录页面
buytime = '2019-04-02 22:33:01'
a = taobao_infos(url,buytime)
a.login()
a.settle()
a.buy_on_time()
