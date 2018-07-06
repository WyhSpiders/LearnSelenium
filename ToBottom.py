from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
# 移动到最底端
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alart("To Bottom")')