from selenium import webdriver
from time import sleep

browzer = webdriver.Chrome('/home/speedweed/Desktop/automation/src/chromedriver')
# need to figure out a way to automate navigations
browzer.get("http://127.0.0.1:5500/test.html")

def automation_2(cover,content):
    content_upload_elment=browzer.find_element_by_xpath('//*[@id="data-assets-interior-file-upload-accepted-extensions"]')
    image_upload_enabler=browzer.find_element_by_xpath('//*[@id="data-cover-choice-accordion"]/div[2]/div/div[1]/a//*[@id="data-cover-choice-accordion"]/div[2]/div/div[1]/a')
    image_upload_content=browzer.find_element_by_xpath('//*[@id="data-assets-cover-file-upload"]')

    content_upload_elment.send_keys(content)
    sleep(1)
    image_upload_enabler.click()
    sleep(1)
    image_upload_content.send_keys(cover)
    sleep(1)
