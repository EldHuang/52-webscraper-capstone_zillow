from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Forms:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://forms.gle/Jhv4CTfazUGUG3EE8")

    def fill_form(self, addr_list, price_list, links_list):
        wait = WebDriverWait(self.driver, 15)

        for house in range(len(addr_list)):
            address = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
                )
            )

            price = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
                )
            )

            link = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
                )
            )

            address.send_keys(addr_list[house])
            price.send_keys(price_list[house])
            link.send_keys(links_list[house])

            submit_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "div[role='button']")
                )
            )
            submit_button.click()

            submit_another_response_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a[href*='viewform?usp=form_confirm']")
                )
            )
            submit_another_response_btn.click()
