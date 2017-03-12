from selenium import webdriver

class testClass():

    def testMethod(self):

        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com")
        driver.quit()

ff = testClass()
ff.testMethod()