import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome('C:/Users/sky99/Desktop/개별연구/sele/chromedriver.exe')
## In the following segment, I show how you can get a list of news article URLs based on a keyword search.
## I use CNN as an example but news source would work.

base_url = u'https://www.cnn.com/search?q=bitcoin&size=200'

browser.get(base_url)
time.sleep(1)

#Finds the container that contains every news article.
main_news_container = browser.find_element_by_class_name('cnn-search__results-list')



title = []


#In main container get 'a'
text_sections = main_news_container.find_elements_by_xpath("//a[@href]")

for elem in text_sections:
    if "/2021/" in elem.get_attribute("href"):
        #this is printing the link
        print(elem.get_attribute("href"))
        #this is printing the Headline
        # url.append(elem.get_attribute("href"))
        print(elem.text)
        if elem.text != '':
            title.append(elem.text)
        


#Find the text body_elements inside the main_news_container
body_elements = main_news_container.find_elements_by_class_name("cnn-search__result-body")

#this is how you get the body body_elements text

# num = int(input('Please enter the number of news articles required.(Enter numbers only) : '))

print(title)

for i in range(0,100):
    with open('{0}.txt'.format(i), 'w', encoding='UTF-8') as fw:
        print("TITLE")
        fw.write(title[i])
        fw.write('. ')
        print("TEXT")
        print(body_elements[i].text)
        fw.write(body_elements[i].text)
        print()

print("Close text file")

