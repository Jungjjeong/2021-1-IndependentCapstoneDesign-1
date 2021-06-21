#셀레니움 관련 라이브러리
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#크롬 드라이버 불러와서 사이트 이동 후 찾고자 하는 내용 검색
driver = webdriver.Chrome()
driver.get("https://edition.cnn.com/")
searchbutton = driver.find_element_by_css_selector(".search-icon").click()
search = driver.find_element_by_id("header-search-bar")
search.send_keys("corona")
search.send_keys(Keys.RETURN)
time.sleep(5)

mainurl = driver.current_url


#화면에 로드 된 기사(10개)의 url 저장

cnt = 0

def getArticles():
    global cnt
    urlists = []
    elems = driver.find_elements_by_xpath("//div[@class='cnn-search__result-thumbnail']/a")
    for elem in elems:
        urls = elem.get_attribute("href")
        print(urls)
        urlists.append(urls)


    for urlist in urlists:
        print("\n\n\n")
        print("################article NUMBER " + str(cnt+1) + "#################")
        print(urlist)

        #url 접속하여 기사 내용 저장
        driver.get(urlist)
        time.sleep(5)

        try:
            article = driver.find_element_by_id("body-text")
            artext = article.text
            print("------------article complete------------")
            #print(artext)
            #텍스트 내용 저장
                #텍스트 파일 생성
            filename = str(cnt+1) + 'test.txt'
        
            f = open(filename,'w',encoding='UTF-8')
            #텍스트 내용 저장
            text = artext
            f.write(text)
            f.close()
            print("###########file made############")

            cnt = cnt + 1
            print(cnt)

        except:
            print("////////NO ARTICLE//////////")
    
    
getArticles()
time.sleep(3)

print("\n\n\n##########################PAGE CHANGE########################\n\n\n")
driver.get(mainurl)
time.sleep(5)
driver.find_element_by_css_selector(".pagination-arrow.pagination-arrow-right.cnnSearchPageLink.text-active").click()
time.sleep(5)
mainurl = driver.current_url
getArticles()

print("\n\n\n##########################PAGE CHANGE########################\n\n\n")
driver.get(mainurl)
time.sleep(5)
driver.find_element_by_css_selector(".pagination-arrow.pagination-arrow-right.cnnSearchPageLink.text-active").click()
time.sleep(5)
getArticles()

    
    
    


    
    
    

