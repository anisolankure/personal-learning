import warnings

class Find:
    def findBy(driver, elementName):        
        warnings.filterwarnings(action="ignore")
        element = driver.find_element_by_name(elementName)
        element.clear()
        return element