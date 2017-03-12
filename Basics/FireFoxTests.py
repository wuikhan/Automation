from selenium import webdriver

class RunnFFTests():

    def test(self):
        driver = webdriver.Firefox()
        driver.get("http://www.google.com")
        driver.quit()

ff = RunnFFTests()
ff.test()
