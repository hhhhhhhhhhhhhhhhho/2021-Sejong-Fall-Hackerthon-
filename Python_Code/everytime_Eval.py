from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import requests
import time
import csv
import pandas as pd
import numpy as np

# CSV파일을 읽고 배열로 변환하기
readList = []
professorList = [[''] for _ in range(10)]
maengFile = 'C:\PythonPractice\Python\해커톤(2021-2학기)\professorList.csv'
yongFile = '/Users/yongcho/Desktop/Project/해커톤/profName.csv'

with open(yongFile, 'r') as f:
    file_read = csv.reader(f)
    for line in f:
        readList.append(line)
    # 과를 포함한 교수님 리스트 (2차원 배열)
    for i in range(10):
        
        if i < 9:
            professorList[i] = readList[i].split(',')
        else :
            list=[]
            list = readList[i].split('\t')   
            
            # 교양 교수님들 중복 제거
            for k in range(len(list)):
                
                if list[k] not in professorList[i]:
                    professorList[i].append(list[k])

    professors = []  # 교수님 전체를 담은 리스트 (1차원 배열)
    for i in range(10):
        for j in range(1, len(professorList[i])):
            if len(professorList[i][j]) < 2:
                continue
            
            professors.append(professorList[i][j])

            if professorList[i][j].endswith(')'): #학과장이면,
                professors[-1] = professors[-1][:3] #학과장 표시 없애줌

            if j == len(professorList[i])-1 and i != 9: #마지막 사람 개행 표시 지우기
                
                professors[-1] = professors[-1][:-1]


yongDriver = '/Users/yongcho/Desktop/Tool/chromedriver'
maengDriver = 'C:\PythonPractice\Python\Web Page Scraping\chromedriver.exe'
yongHeader = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
maengHeader = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'

headers = {'User-Agent': yongHeader}
browser = webdriver.Chrome(yongDriver)  # './chromedriver'
url = 'https://everytime.kr/'
browser.get(url)

# 지정한 위치로 스크롤 하기
# browser.execute_script("window.scrollTo(0,300)") #300크기만큼 스크롤 내림
# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 파일 오픈
# filename = ""
# file = open(filename, "w", encoding="utf-8-sig",  newline="")
# csvfile = csv.writer(file) #writer로 파일 쓰기

# feature = []
# csvfile.writerow(feature)

# 로그인
browser.find_element_by_link_text("로그인").click()
id = 'dragon706'
psw = 'yj028020'
browser.find_element_by_xpath('//*[@id="container"]/form/p[1]/input').send_keys(id)
browser.find_element_by_xpath('//*[@id="container"]/form/p[2]/input').send_keys(psw)
browser.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

# 강의 평가 페이지
browser.find_element_by_xpath('//*[@id="menu"]/li[3]/a').click()

# 강평 제외 다른 내용 다 담을 dataframe
df = pd.DataFrame([], columns=['과목이름', '교수님', '강의평가'])

for pro in professors:
    # 과목명 입력
    professorName = pro

    # 이전 검색어 있으면 지우고
    browser.find_element_by_class_name('keyword').clear()
    browser.find_element_by_class_name('keyword').send_keys(professorName)
    browser.find_element_by_class_name('submit').click()

    # 로딩까지 기다리기
    browser.implicitly_wait(5)
    
    # 해당 과목 교수별 강의평가 클릭
    
    res = requests.get(url + 'lecture/search/' + professorName, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(browser.page_source, 'lxml')

    star = browser.find_elements_by_class_name('lecture')

    className = 0  # 과목 이름
    classEval = []  # 강평


    for k in range(1, len(star) + 1):  # 별점이 있는 것들만 반복

        # 로딩까지 기다리기
        browser.implicitly_wait(3)
        isRate = browser.find_element_by_xpath(f'//*[@id="container"]/div/a[{k}]/p/span/span').get_attribute('style')
        # soup2 = BeautifulSoup(browser.page_source, 'lxml')
        browser.implicitly_wait(3)

        if isRate[7] == '0':
            break

        # twoname = browser.find_elements_by_class_name('professor')
        if k == 8 or k == 16 or k == 24 or k == 32:
            browser.execute_script("window.scrollTo(0,400)")

        browser.find_element_by_xpath(f'//*[@id="container"]/div/a[{k}]').click()
        browser.implicitly_wait(3)

        
        className = (browser.find_element_by_xpath('//*[@id="container"]/div[2]/h2').text)
        
        # 강평DD
        classEval = ([e.text.replace("\n", "") for e in browser.find_elements_by_class_name('text')])
        classEval = ','.join(classEval)
        df = df.append(pd.Series([className, professorName, classEval],
                            index=df.columns), ignore_index=True)
        
        
        
        browser.back()
    

df.to_csv('ClassEval.csv', encoding='utf-8-sig')