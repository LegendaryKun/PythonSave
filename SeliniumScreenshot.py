# Selinium 实现截屏截取登录页面的验证码
from PIL import Image
from selenium import webdriver

url = 'http://202.194.116.31/'  #选课系统登录页面
driver = webdriver.Chrome()
driver.maximize_window()  # 将浏览器最大化
driver.get(url)
# 截取当前网页并放到F盘命名为printscreen，该网页有我们需要的验证码
driver.save_screenshot(r'F:\Python\program\printscreen.png')

im = Image.open(r'F:\Python\program\printscreen.png')  # 转换为图片的形式
im.show()  # 展示验证码

imgelement = driver.find_element_by_id('vchart')  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
size = imgelement.size  # 获取验证码的长宽
rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
          int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
i = Image.open(r'F:\Python\program\printscreen.png')  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
#frame4.save(r'F:\Python\program\save.jpg') # 保存我们接下来的验证码图片 进行打码
frame4.save(r'F:\Python\program\save.png')   #由于运行时不能把png改为jpg,所以我修改为png
im = Image.open(r'F:\Python\program\save.png')
im.show()
driver.close()
