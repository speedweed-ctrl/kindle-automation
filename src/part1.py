from time import sleep
from selenium import webdriver
browzer = webdriver.Chrome('/home/speedweed/Desktop/automation/src/chromedriver')
# need to figure out a way to automate navigations
browzer.get("http://127.0.0.1:5500/test.html")
sleep(1)


def automation_1(data,browzer):
    injection_data_title=data['title']
    injection_data_auth=data['auth']
    injection_data_dis=data['dis']
    
    #get the element to enject code with
    title_element=browzer.find_element_by_id('data-title')
    author_element=browzer.find_element_by_id('data-primary-author-first-name')
    copy_write_element=browzer.find_element_by_id('non-public-domain')
    keyword_element=browzer.find_element_by_id('data-keywords-0')
    cat_action_element=browzer.find_element_by_xpath('//*[@id="checkbox-fiction-classics"]')
    cat_button_ellement=browzer.find_element_by_xpath('//*[@id="checkbox-fiction_action-and-adventures"]')

    #inject the data
    title_element.send_keys(injection_data_title)
    sleep(1)
    author_element.send_keys(injection_data_auth)
    sleep(1)
    copy_write_element.click()
    sleep(1)
    keyword_element.send_keys(injection_data_auth)
    sleep(1)
    cat_button_ellement.click()
    sleep(1)
    cat_action_element.click()
    sleep(1)
    
    save_button=browzer.find_element_by_xpath('//*[@id="category-chooser-ok-button"]/span/input')
    save_button.click
