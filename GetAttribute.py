# -*- coding: utf-8 -*-
from selenium import webdriver
from lxml import etree

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element_by_id('zh-top-link-logo')
# 获取对象class属性的值
print(logo.get_attribute('class'))
line = browser.find_element_by_class_name('zu-top-add-question')
# 获取对象的文本
print(line.text)
# 获取对象的id
print(line.id)
# 获取对象的相对位置
print(line.location)
# 获取对象的标签名称
print(line.tag_name)
# 获取节点的宽高
print(line.size)
print(line)
#print(browser.page_source)
xpathObj = etree.HTML(browser.page_source)
zu_id = xpathObj.xpath('//button[@class="zu-top-add-question"]/@id')
print(zu_id)
browser.close()