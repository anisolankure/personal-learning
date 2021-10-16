from selenium import webdriver

class Provider:
    def seleniumdriver(type):
        if(type == "chrome"):
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            return webdriver.Chrome('chromedriver', options=options)
        else:
            raise ValueError("Invalid selenium driver provided")
        