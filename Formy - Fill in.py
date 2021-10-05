#import Selenium WebDriver library(for Chrome usage):
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#specify the ChromeDriver location
chrome = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

#import "Sleep" library
from time import sleep

#navigate to URL
chrome.get("https://formy-project.herokuapp.com/form")

#maximize Chrome window
chrome.maximize_window()

#identifying the elements and sending data to fill in the form

chrome.find_element_by_xpath("//input[@placeholder='Enter first name']").send_keys("John")
chrome.find_element_by_id("last-name").send_keys("Doe")
chrome.find_element_by_id("job-title").send_keys("Software Engineer")
chrome.find_element_by_id("radio-button-1").click()
chrome.find_element_by_xpath("//input[@value='checkbox-1']").click()

select = Select(chrome.find_element_by_id('select-menu'))
select.select_by_index(2)

dateField = chrome.find_element_by_id('datepicker')
dateField.click()
dateField.send_keys("04102021")
dateField.send_keys(Keys.RETURN)

#Click Submit
chrome.find_element_by_link_text("Submit").click()

#assert alert.is_displayed()
assert chrome.page_source.find("thanks")

#use sleep
sleep(2)

#close Chrome browser
chrome.close()