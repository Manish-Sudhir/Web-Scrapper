from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

"""
Generic Scrapper class that hosts functions that are to be used by the scrapper
"""
class Scrapper:
    def __init__(self,url: str='https://www.transfermarkt.com/', headless: bool =True):
        if headless:
            print("Starting...")
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument('--headless')
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximised")
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url) 

    def accept_cookies(self, xpath: str = "//button[contains(@title,'ACCEPT ALL')]"):
        """
        Finds and clicks the "accept cookies" button in the frame

        parameters:
        xpath : str
                The Xpath of the accept cookies button in the frame
        """
        WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@id="sp_message_iframe_575843"]')))
        accept_cookies= WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath)))
        accept_cookies.click()
    
    def click_element(self, xpath: str):
        """
        Clicks a element

        parameters:
        xpath : str
                The Xpath of the element
        """

        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def find_elements_in_container(self, xpath_container: str, 
                                    tag_elements: str) -> list:
        """
        Clicks a element in a container 

        parameters:
        xpath_container : str
                The Xpath of the container
        tag_elements : str
                The Xpath of the elements to be found in the container
        """

        container = self.driver.find_element(By.XPATH, xpath_container)
        elements_in_container = container.find_elements(By.XPATH, f'./{(tag_elements)}')

        return elements_in_container

"""
Child class of the Scrapper class
This class is made according to the use case of the web-scrapper
This project scrapes a football analytics site
"""
class PlayerScrapper(Scrapper):
    def search_team(self,
                    team:str,
                    xpath_search_bar: str = '//*[@id="schnellsuche"]/input[1]'):
        """
        Function that searches for a particular team on the search bar

        parameters:
        team : str
                name of the team to be searched
        xpath_search_bar : str
                xpath of the search bar on the webpage
        """
        self.accept_cookies()
        time.sleep(1)
        print("Searching team..")
        search_bar = self.driver.find_element(By.XPATH, xpath_search_bar)
        search_bar.click()
        time.sleep(1)
        search_bar.send_keys(team)
        search_bar.click()
        search_bar.submit()
        time.sleep(1)
        top_result = self.driver.find_element(By.XPATH, '//*[@id="yw1"]/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/a')
        top_result.click()

    def get_info(self):
        """
        Function that scrapes the team information from the webpage 
        """
        # Storing data retrieved from webpage table into variables
        kit_numbers = self.driver.find_elements(By.XPATH, '//table[@class="items"]/tbody/tr/td[1]')
        player_names = self.driver.find_elements(By.XPATH, '//table[@class="items"]/tbody/tr/td[2]')
        player_dob = self.driver.find_elements(By.XPATH, '//table[@class="items"]/tbody/tr/td[4]')
        market_value = self.driver.find_elements(By.XPATH, '//table[@class="items"]/tbody/tr/td[6]')
        name=[]
        position=[]
        # Player name column on webpage table holds player name and position
        # So splitting that information here into different variables
        for p in player_names:
            hold = p.text
            hold.split('\n')
            name.append(hold.split('\n')[0])
            position.append(hold.split('\n')[1])

        # Create pandas dataframe with scrapped informationo
        df_team_info = pd.DataFrame(columns=['Kit Number', 'Name', 'Position', 'Date Of Birth/Age', 'Market Value'])
        for i in range(len(kit_numbers)):
            df_team_info = df_team_info.append({'Kit Number': kit_numbers[i].text,
                                                'Name': name[i],
                                                'Position': position[i],
                                                'Date Of Birth/Age': player_dob[i].text,
                                                'Market Value': market_value[i].text}, ignore_index=True)
        print("Done!")
        return df_team_info