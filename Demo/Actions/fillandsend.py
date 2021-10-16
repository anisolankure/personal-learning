from selenium.webdriver.common.keys import Keys

class FillAndEnter:
    def send(element, keys):
        element.send_keys(keys)
        element.send_keys(Keys.RETURN)
        return element