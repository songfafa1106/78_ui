from selenium import webdriver
import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)#智能等待

def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()

def login_fun(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()

def sear_fun(driver,url,username,password,key):
    open_url(driver,url)
    login_fun(driver,username,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
    id_frame = id_li+"-frame"
    driver.switch_to.frame(id_frame)
    driver.find_element_by_id("searchNumber").send_keys(key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(2)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num
