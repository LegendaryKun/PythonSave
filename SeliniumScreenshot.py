# encoding:utf-8
from PIL import Image
from selenium import webdriver

url = 'https://weibo.com/login.php?spm=a2107.1.0.0.71ae11d9wHU59y&entry=taobao&goto=https%3A%2F%2Flogin.taobao.com%2Faso%2Ftvs%3Fdomain%3Dweibo%26sid%3Dc0f74b7980b0d344e3568e471afa3e94%26target%3D687474703A2F2F6D656D626572312E74616F62616F2E636F6D2F6D656D6265722F66726573682F776569626F5F62696E645F6D616E6167656D656E742E68746D3F73706D3D61317A30382E312E302E302E356566393937386254536A63656B&goto2=http%3A%2F%2Fmember1.taobao.com%2Fmember%2Ffresh%2Fweibo_bind_management.htm%3Fspm%3Da1z08.1.0.0.5ef9978bTSjcek'
driver = webdriver.Chrome()
driver.maximize_window()  # 将浏览器最大化
driver.get(url)
# 截取当前网页并放到E盘下命名为printscreen，该网页有我们需要的验证码
driver.save_screenshot(r'F:\Python\program\printscreen.png')

im = Image.open(r'F:\Python\program\printscreen.png')  # 转换为图片的形式
im.show()  # 展示验证码

imgelement = driver.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
size = imgelement.size  # 获取验证码的长宽
rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
          int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
i = Image.open("E:\\printscreen.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4.save('E:\\save.jpg') # 保存我们接下来的验证码图片 进行打码
driver.close()
