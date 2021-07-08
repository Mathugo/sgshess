import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from time import sleep

USERNAME = 'hugomat'
PASSWORD = 'qf5vw89fz14ap04' 

# SIMPLE ROUTINE LOGIN -> VACANT OBJECTS -> FILTER -> LIST VACANT OBJECTS


class browsing_bot():
    def __init__(self, username, password):
        self.BASE_URL = 'https://www.sgs.se/Mina-sidor/Login?return=https://www.sgs.se/mina-sidor/mina-%C3%A4renden?sc_lang=en'
        self.VACANT_OBJECT_URL = 'https://www.sgs.se/mina-sidor/lediga-objekt?sc_lang=en'
        
        self.username = username
        self.password = password
        
        self.chromedriver = 'chromedriver.exe'
        self.browser = webdriver.Chrome(self.chromedriver)
    
    def login(self):
        self.browser.get(self.BASE_URL)
        username = self.browser.find_element_by_name("User")
        username.send_keys(self.username)

        password = self.browser.find_element_by_name("Password")
        password.send_keys(self.password)

        password.send_keys(Keys.RETURN)
        sleep(3)
        self.browser.get(self.VACANT_OBJECT_URL)

    # FILTER
    def my_filter(self):
        sleep(5)
        # switch to filter frame
        filter_frame = self.browser.find_element_by_id("momentum")
        self.browser.switch_to_frame(filter_frame)

        # display toggle btn
        toggle_search_area = self.browser.find_element_by_id("toggle-seekarea")
        toggle_search_area.send_keys(Keys.ENTER)
        sleep(2)

        # but search area
        #center_btn = self.browser.find_element_by_css_selector("div.")
        #center_btn = self.browser.find_element_by_xpath("//ins[contains(@class, 'jstree-unchecked jstree-closed', 'jstree-icon')").click()
        
        center_expand_btn = self.browser.find_elements_by_class_name("jstree-icon").click()

        #self.browser.find_element_by_xpath("//option[text()='Centrum']").click()

        do_search_btn = self.browser.find_element_by_id("doSearch")
        do_search_btn.send_keys(Keys.ENTER)


        #self.browser.get('https://marknad.sgs.se/pgSearchResult.aspx#&seekAreaMode=extended')
        #toggle_seekarea = self.browser.find_element_by_id("toggle-seekarea")
        #toggle_seekarea.send_keys(Keys.ENTER)

        #actions = ActionChains(self.browser)
        #actions = actions.send_keys(Keys.TAB* 13 ) # 13 TAB to filter by area
        #actions = actions.send_keys(Keys.DOWN) # Filter center
        #actions = actions.send_keys(Keys.TAB * 3) # TAB To Search
        #actions = actions.send_keys(Keys.ENTER)
        #actions.perform()

    def close(self):
        sleep(1000)
        self.browser.close()

browser = browsing_bot(USERNAME, PASSWORD)
browser.login()


browser.my_filter()
browser.close()
