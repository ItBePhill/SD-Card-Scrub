import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
destdir = "C:/Users/phill/Desktop/desmume-win-x64/Roms"
filearray = os.listdir("E:/")
ndsarray = []
savarray = []
for i in filearray:
    if os.path.splitext(i)[1] == ".sav":
        savarray.append(i)
os.environ['PATH'] += "/path/to/chromedriver"
driver = webdriver.Chrome()
driver.get("https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20DS%20(Decrypted)/")
driver.maximize_window()
time.sleep(5)
for i in savarray:
    try:
        # Finding the search field by id
        input = webdriver.find_element_by_id("searchInput")
     
    # Sending input text to search field
        input.send_keys(i)
     
    # Pressing enter to search input text
        input.send_keys(Keys.ENTER)
        time.sleep(5)
    finally:
        button = driver.find_element("link text", os.path.splitext(i)[0])
        button.click()


    