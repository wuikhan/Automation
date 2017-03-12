from selenium import webdriver

baseUrl = "https://www.facebook.com"
driver = webdriver.Firefox()
driver.get(baseUrl)
driver.quit()
