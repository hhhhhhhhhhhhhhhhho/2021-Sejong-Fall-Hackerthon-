from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

yongDriver = '/Users/yongcho/Desktop/Tool/chromedriver'
maengDriver  = 'C:\PythonPractice\Python\Web Page Scraping\chromedriver.exe'
yongHeader = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
maengHeader = ''

headers = {'User-Agent' : yongHeader}
browser = webdriver.Chrome(yongDriver) #'./chromedriver'
url = 'http://www.sejong.ac.kr/college/index.html'
browser.get(url)

#지정한 위치로 스크롤 하기
# browser.execute_script("window.scrollTo(0,300)") #300크기만큼 스크롤 내림
#화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#파일 오픈
filename = "profName.csv"
file = open(filename, "w", encoding="utf-8-sig",  newline="")
csvfile = csv.writer(file) #writer로 파일 쓰기
            

#기본틀
profList = [[],
            ['컴퓨터공학과'],
            ['소프트웨어학과'],
            ['정보보호학과'],
            ['데이터사이언스학과'],
            ['지능기전공학부'],
            ['디자인이노베이션'],
            ['만화애니메이션텍'],
            ['인공지능학과'],
            ['대양휴머니티칼리지']]

divXpath = '//*[@id="content"]/div[10]/dl/dd/ul/li'

#소융대
for i in range(1,8):

    # 과목마다 Xpath가 달라서 세갈래로 구분지음
    if i < 5:
        #학과페이지로 이동
        browser.find_element_by_xpath(divXpath+f"[{i}]/a").click()
        
        #교수 소개 페이지로 이동
        introProf = '//*[@id="content"]/div[4]/div/ul/a/li'
        browser.find_element_by_xpath(introProf).click()

        #soup request 갱신
        res = requests.get(browser.current_url, headers = headers)
        res.raise_for_status()
        soup = BeautifulSoup(browser.page_source, 'lxml')

        #긁어오기
        time.sleep(1)
        nameList = soup.find("div", "prof_list").find_all("h4")
        
        #하나씩 뺴서 리스트에 담기
        for name in nameList:
            profList[i].append(name.get_text())
        print(profList[i])
        
        #두번 뒤로가기
        browser.back()
        browser.back()

    #디이노, 만애 (창의소프트)
    elif i == 6:
        for j in range(0,2):
            #학과페이지로 이동
            browser.find_element_by_xpath(divXpath+f"[{i}]/a[1]/strong").click()   
            
            #디이노/만애 페이지로 이동
            divd2page = '//*[@id="content"]/div[4]/ul/a'
            index = 1 + j

            browser.find_element_by_xpath(divd2page+f"[{index}]/li").click()

            #교수 소개 페이지로 이동
            
            introProf = '//*[@id="content"]/div[4]/div/ul/a/li'
            browser.find_element_by_xpath(introProf).click()

            #soup request 갱신
            res = requests.get(browser.current_url, headers = headers)
            res.raise_for_status()
            soup = BeautifulSoup(browser.page_source, 'lxml')
            #긁어오기
            time.sleep(1)
            nameList = soup.find("div", "prof_list").find_all("h4")
            
            for name in nameList:
                profList[i + j].append(name.get_text())
            print(profList[i + j])
            
            browser.back()
            browser.back()
            browser.back()
        
    
    #지기전, 인공지능
    else :
        
        browser.find_element_by_xpath(divXpath+f"[{i}]/a").click()
        
        #교수 소개 페이지로 이동
        introProf = '//*[@id="content"]/div[4]/ul/a/li'
        browser.find_element_by_xpath(introProf).click()

        #soup request 갱신
        res = requests.get(browser.current_url, headers = headers)
        res.raise_for_status()
        soup = BeautifulSoup(browser.page_source, 'lxml')

        #긁어오기
        time.sleep(1)
        nameList = soup.find("div", "prof_list").find_all("h4")

        if i == 7:
            i+=1

        for name in nameList:
            profList[i].append(name.get_text())
        
        browser.back()
        browser.back()

#대양휴머
humanDiv = '//*[@id="content"]/div[13]/dl/dd/ul/li/a/strong'
browser.find_element_by_xpath(humanDiv).click()
introProf = '//*[@id="content"]/div[4]/ul/a/li'
browser.find_element_by_xpath(introProf).click()

#soup request 갱신
res = requests.get(browser.current_url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(browser.page_source, 'lxml')

time.sleep(1)
nameList = soup.find("div", "prof_list").find_all("h4")

for name in nameList:
    profList[9].append(name.get_text())

#csv 만들기
csvfile.writerows(profList)