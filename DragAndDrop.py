from selenium import webdriver
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
# 定位到窗口，可以用id或者name来定位
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
# 动作执行
actions.perform()
