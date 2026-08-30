from selenium import webdriver

class Forms:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://forms.gle/Jhv4CTfazUGUG3EE8")

    def fill_form(self, addr_list, price_list, links_list):
        pass