from selenium import webdriver
import time
driver=webdriver.Chrome() #打开浏览器
time.sleep(2)
driver.get("http://taobao.com")
time.sleep(2)
driver.get("http://baidu.com")
driver.maximize_window()#最大化浏览器
time.sleep(2)
driver.back()#返回到上ー个页面
time.sleep(2)
driver. forward()#前进道下一个页面
time.sleep(2)
driver. refresh()#刷新页面
#driver.quit()#关闭 Chromedriverf服务，关闭整个浏览器
#driver. close()#多个窗口，关闭当前窗口，不会关闭浏览器
