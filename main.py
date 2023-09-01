from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from browser import *


if __name__ == "__main__":
    browser = browser()
      
    browser.launchbrowser()
    
    

    
    for i in range(2, 40):
        #browser.description()
        browser.Scrape()
        browser.next(page=i)
    browser.corrections()

                 
    
    
    