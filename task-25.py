"""
using python selenium , explicit wait, expected condition and chrome driver do Fill the data given in the input Boxes ,select Boxes and drop down menu on the menu and do s search
"""


# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Exception
from selenium.common.exceptions import NoSuchElementException
# Action Chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver.common.keys import Keys


class FillData:
    def __init__(self, url="https://www.imdb.com/search/name/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        self.driver.implicitly_wait(10)

    def boot(self):
        """
        This method open the url and maximize window
        """
        self.driver.get(self.url)
        self.wait.until(EC.url_to_be(self.url))
        self.driver.maximize_window()
        for _ in range(9): # using Action Chains in loop for scroll down the page
            self.action.send_keys(Keys.DOWN).perform()

    def quit(self):
        """
        This Method  close the Browser
        :return:None
        """
        self.driver.quit()

    def sendData(self):
        """
           This Method Find The Web Element And Sent Keys To Input Box
        """

        self.boot()
        try:

            # name input
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[1]/label"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input"))).send_keys("Anna Helene paquin")
            print("name is filled")
            # BirthDate input
            for _ in range(3):
                self.action.send_keys(Keys.DOWN).perform()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[1]/label"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/input"))).send_keys("24-7-1982")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/input"))).send_keys("4-3-2024")
            print("BirthDate is filled")

            # Birthday Input

            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[3]/div[1]/label"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[3]/div[2]/div/div/div/div/div/div/input"))).send_keys("24-7")
            print("Birthday entered")

            # see Result Button
            for _ in range(3): # using action chains in loop for scroll down the page
                self.action.send_keys(Keys.DOWN).perform()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button"))).click()
            expected_result="https://www.imdb.com/search/name/?name=Anna%20Helene%20paquin&birth_date=1982-07-24,2024-03-04"
            actualurl=self.driver.current_url
            print(actualurl)
            assert expected_result == actualurl
            print("data is filled correctly")


        except NoSuchElementException as e:
            # if element not find in Webpage then this block of will execute
            print("Error:Element is not visible", e)




obj = FillData()
obj.sendData()

