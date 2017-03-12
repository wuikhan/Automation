from selenium import webdriver

class findElement():

    def testMethod(self):

        baseURL = "https://www.facebook.com"
        driver = webdriver.Firefox()
        driver.get(baseURL)

        elementByID = driver.find_element_by_id("email")
        if elementByID is not None:
            print("We found an element by id")

        elementByName = driver.find_element_by_name("pass")
        if elementByName is not None:
            print("We found an element by Name")

        driver.find_element_by_class_name("")



        driver.quit()

ff = findElement()
ff.testMethod()