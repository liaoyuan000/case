from selenium import webdriver

class Case:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("www.baidu.com")
    def get_id(self):
        pass
    def get_classname(self):
        pass




if __name__ == '__main__':
    a=Case()