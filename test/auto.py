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

'''

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