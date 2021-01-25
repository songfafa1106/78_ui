from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)#智能等待
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()
#获取页面标题
page_title = driver.title
if page_title=="柠檬ERP":
    print("这个页面标题是：{}".format(page_title))
else:
    print("这个用例不通过！")

#输入用户名、密码，进行登录操作
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id("btnSubmit").click()

#确认登录用户名
page_name = driver.find_element_by_xpath("//p").text
if page_name =="测试用户":
    print("这个登录用户是：{}".format(page_name))
else:
    print("这个用例不通过！")


'''切换iframe子页面.switch_to.
driver.find_element_by_xpath("//span[@class='l-btn-left']").click()#找不到元素，html页面的嵌套
driver.switch_to.frame("tabpanel-0c512b4bab-frame")#id是变化的，不能直接取值（变化:无规律的数字）'''
driver.find_element_by_xpath("//span[text()='零售出库']").click()
id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')#找到元素获取id属性
id_frame = id_li+"-frame"
driver.switch_to.frame(id_frame) #通过iframe id进行iframe页面切换
# driver.switch_to(driver.find_element_by_xpath("//p[@id='{}']".format(id_frame)))  #xpath定位
#子页面操作
driver.find_element_by_id("searchNumber").send_keys("712")#找到单据编号输入框，输入内容
driver.find_element_by_id("searchBtn").click()#点击搜索
time.sleep(2)
#获取订单编号
num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text#获得单据编号号码
print(num)
if "712"in num:
    print("搜索用例通过")
else:
    print("搜索失败")