import imp
import fetcData
import part1
from selenium import webdriver
browzer = webdriver.Chrome('/home/speedweed/Desktop/automation/src/chromedriver')
# need to figure out a way to automate navigations
browzer.get("http://127.0.0.1:5500/test.html")

data=fetcData.fetch_description_data()[1]
part1.automation_1(data,browzer)
