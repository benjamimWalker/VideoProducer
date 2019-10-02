from selenium import webdriver
from time import sleep
import pyperclip
def get_tags(term):
    chrome = webdriver.Chrome(executable_path='/home/benjamim/Documentos/chromedriver')

    chrome.get('https://tagsyoutube.com/home')
    sleep(1.8)

    chrome.find_element_by_id('tagsSearch').send_keys(term)
    chrome.find_element_by_id('getTags').click()

    sleep(10)

    chrome.find_element_by_class_name('custom-control-description').click()
    sleep(0.2)
    chrome.find_element_by_id('copyTags').click()
    sleep(0.2)
    chrome.find_element_by_id('copytoclipboard').click()
    sleep(0.7)
    sleep(80)
