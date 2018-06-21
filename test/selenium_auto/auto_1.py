#!user/bin/python
#_*_ coding: UTF-8 _*_
#author:wangjuan
'''
#1.访问网页
from selenium import webdriver   #导入webdriver包
driver = webdriver.Chrome()  # 导入实例
driver.get("http://www.baidu.com") #打开url
print(driver.page_source)
driver.close()

#2.查找元素
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.taobao.com")
input_first=driver.find_element_by_id("q")
input_second=driver.find_element_by_css_selector("#q")
input_third=driver.find_element_by_xpath('//*[@id="q"]')
print (input_first)
print (input_second)
print (input_third)

#3.元素定位
from selenium import webdriver
import time
driver=webdriver.Chrome()
#driver.find_element_by_name('wd').send_keys("selenium")
#driver.find_element_by_tag_name("input").send_keys("selenium")
#driver.find_element_by_css_selector("#kw").send_keys("selenium")
#driver.find.element_by_css_selector("a.mnav").click()
driver.get('http://baidu.com')
driver.maximize_window()
driver.implicitly_wait(300)
date =driver.find_element_by_id("cp").text
print dat

4#键盘按键
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("http://baidu.com")
#driver.find_element_by_id("username").clear()
#driver.find_element_by_id("username").send_keys("wangjuan001")
#driver.find_element_by_id("username").send_keys(Keys.TAB)
#time.sleep(3)
#driver.find_element_by_id("password").send_keys("1q2w3e4r")
#driver.find_element_by_id("password").send_keys(Keys.ENTER)
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(1)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
driver.find_element_by_id("kw").send_keys(u"python")
driver.find_element_by_id("su").click()

#5.鼠标按键
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
qqq=driver.find_element_by_xpath("")
ActionChains(driver).context_click(qqq).perform()

'''

#6.下拉框操作
from selenium import  webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_name("tj_settingicon")
driver.find_element_by_xpath("//a[contains(class,'setpref')]")
driver.find_element_by_id("nr")
driver.find_element_by_xpath("//option[@value='10']")
driver.find_element_by_xpath("//a[contains(class,'prefpanelgo')]")
time.sleep(2)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()



