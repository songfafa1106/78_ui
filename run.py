from common import UI_method
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

url =test_data.data['url']
username =test_data.data["username"]
password = test_data.data["password"]
key = test_data.data.get("key")
print(url,username,password,key)

num = UI_method.sear_fun(driver,url,username,password,key)
if key in num:
    print("搜索用例通过")
else:
    print("搜索失败")