from selenium.webdriver.common.by import By

class Click:
    def findByClassAndClick(driver, elementName):        
        element = driver.find_element_by_class_name(elementName)
        element.click()        
        return element