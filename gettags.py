from selenium import webdriver
from time import sleep

def get_tags_text(term):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    chrome = webdriver.Chrome(executable_path='/home/benjamim/Documentos/chromedriver', chrome_options=options)
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
    sleep(1)
    frase = chrome.find_element_by_id('finalTags').text.replace('x', ',').replace(' , ', ',')
    frase = frase[0:-2]

    return frase


def tratafrase(term):
    frase = get_tags_text(term)
    frase = frase.split(',')
    while len(frase) > 19:
        frase.pop()
    return ','.join(frase)
