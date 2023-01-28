from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.ID, "num1")
    input1.click()
    input2 = browser.find_element(By.ID, 'num2')
    input2.click()
    x = input1.text
    y = input2.text
    s = str(int(x)+int(y))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s)
    option3 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    option3.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()