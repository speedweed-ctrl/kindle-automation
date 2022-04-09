from gettext import find
from selenium import webdriver
from time import sleep

browzer = webdriver.Chrome('/home/speedweed/Desktop/automation/src/chromedriver')
# need to figure out a way to automate navigations
browzer.get("http://127.0.0.1:5500/test.html")

def automation_1(data):
    injection_data_title=data['title']
    injection_data_auth=data['auth']
    injection_data_dis=data['dis']
    #need to add the discription
    #for that i need to find the correct node element
    #injection_code=f"document.getElementById('data-title').value={injection_data_title} \n document.getElementById('data-primary-author-first-name').value={injection_data_auth}"
    #get the element to enject code with
    title_element=browzer.find_element_by_id('data-title')
    author_element=browzer.find_element_by_id('data-primary-author-first-name')
    copy_write_element=browzer.find_element_by_id('non-public-domain')
    keyword_element=browzer.find_element_by_id('data-keywords-0')
    cat_classic_element=browzer.find_element_by_id('checkbox-fiction-classics')
    cat_action_element=browzer.find_element_by_xpath('//*[@id="checkbox-fiction-classics"]')
    cat_button_ellement=browzer.find_element_by_xpath('//*[@id="checkbox-fiction_action-and-adventures"]')

    #inject the data
    title_element.send_keys(injection_data_title)
    sleep(3)
    author_element.send_keys(injection_data_auth)
    sleep(3)
    copy_write_element.click()
    sleep(3)
    keyword_element.send_keys(injection_data_auth)
    sleep(3)
    cat_button_ellement.click()
    sleep(3)
    cat_action_element.click()
    sleep(3)
    cat_classic_element.click()
    sleep(3)
    #save_button=browzer.find_element_by_xpath('//*[@id="category-chooser-ok-button"]/span/input')
    #save_button.click