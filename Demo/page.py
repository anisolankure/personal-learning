from Actions.find import Find
from Actions.fillandsend import FillAndEnter
from Actions.click import Click
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class AutomationTest:
    def run(driver, url, elementName, searchText):
        driver.get(url)        
        search_bar = Find.findBy(driver, elementName)
        FillAndEnter.send(search_bar, searchText) 
        return driver

    def runandclick(driver, url, elementName):
        driver.get(url)
        Click.findByClassAndClick(driver, elementName)
        return driver    
