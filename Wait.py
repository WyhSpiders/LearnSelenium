from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# 隐式等待
browser.implicitly_wait(2)
browser.get('https://www.zhihu.com/explore')
line = browser.find_element_by_class_name('zu-top-add-question')
print(line)
browser.close()

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
# 显式等待，10秒内加载出来返回该节点，超过10秒抛出异常
wait = WebDriverWait(browser, 10)
line = wait.until(EC.presence_of_element_located((By.ID, 'q')))
buttom = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(line, buttom)
browser.close()
