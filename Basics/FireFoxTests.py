from selenium import webdriver

#class
class RunnFFTests():

    #method
    def test(self):
        baseUrl = "https://www.facebook.com"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByIf = driver.find_element_by_id("email")

        if elementByIf is not None:
            print("We found an element by Id")

        elementByName = driver.find_element_by_name("email")
        if elementByName is not None:
            print("We found an element by Name")


ff = RunnFFTests()
ff.test()