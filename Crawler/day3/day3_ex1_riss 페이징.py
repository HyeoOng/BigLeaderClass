# riss.kr 에서 특정 키워드로 논문 / 학술 자료 검색하기
#Step 1. 필요한 모듈을 로딩합니다                  
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# import chromedriver_autoinstaller as ca
import pandas as pd 
import time 

#Step 2. 사용자에게 검색 관련 정보들을 입력 받고 3. 파일 이름 정하기
query_txt ='빅데이터'
ft_name = "c:\\Users\\Hyewon\\BigLeader\\Crawler\\day3\\riss.txt"
fc_name = "c:\\Users\\Hyewon\\BigLeader\\Crawler\\day3\\riss.csv"
fx_name = "c:\\Users\\Hyewon\\BigLeader\\Crawler\\day3\\riss.xls"
collect_cnt = 50

#Step 4. 크롬 드라이버 설정 및 웹 페이지 열기
driver = webdriver.Chrome()
driver.get('https://www.riss.kr/')

# 팝업창 닫기
main = driver.window_handles
for handle in main:
    if handle != main[0]:
        driver.switch_to.window(handle)
        driver.close()

driver.switch_to.window(main[0])
driver.maximize_window()

time.sleep(2)

#Step 5. 자동으로 검색어 입력 후 6 학위논문 클릭
driver.find_element(By.ID,'query').send_keys(query_txt+ '\n')
driver.find_element(By.LINK_TEXT,'학위논문').click()
time.sleep(2)

#Step 8. 총 검색 건수를 보여주고 수집할 건수 입력받기
import math
soup_1 = BeautifulSoup(driver.page_source, 'html.parser')
total_cnt = soup_1.find('div','searchBox pd').find('span','num').get_text()
print('키워드 %s (으)로  %s 건 검색' %(query_txt,total_cnt))
collect_page_cnt = math.ceil(collect_cnt / 10)

#Step 9. 각 항목별로 데이터를 추출하여 리스트에 저장하기
no2 = [ ]        #번호 저장
title2 = [ ]     #논문제목 저장
writer2 = [ ]    #논문저자 저장
org2 = [ ]       #소속기관 저장
no = 1

for a in range(1, collect_page_cnt + 1) :
    
    soup_2 = BeautifulSoup(driver.page_source, 'html.parser', from_encoding='utf-8')
    content_2 = soup_2.find('div','srchResultListW').find_all('li')
    
    for b in content_2 : 
        #1. 논문제목 있을 경우만
        try :
            title = b.find('p','title').text
        except :
            continue
        else :
            f = open(ft_name, 'a' , encoding="UTF-8")
            
            print('1.번호:',no)
            no2.append(no)
            f.write('\n'+'1.번호:' + str(no))

            print('2.논문제목:',title)
            title2.append(title)
            f.write('\n' + '2.논문제목:' + title)
            
            writer = b.find('span','writer').get_text()
            print('3.저자:',writer)
            writer2.append(writer)
            f.write('\n' + '3.저자:' + writer)

            org = b.find('span','assigned').get_text()
            print('4.소속기관:' , org)
            org2.append(org)
            f.write('\n' + '4.소속기관:' + org + '\n')
            
            f.close( )
            
            no += 1
            print("\n")
            
            if no > collect_cnt :
                break

            time.sleep(2)        # 페이지 변경 전 1초 대기 

    a += 1 
    b = '{}'.format(a)

    try :
        driver.find_element(By.LINK_TEXT ,b).click() 
        time.sleep(1)
    except :
        driver.find_element(By.LINK_TEXT('다음 페이지로')).click()
        time.sleep(1)
        
print("요청하신 작업이 모두 완료되었습니다")

# Step 10. 수집된 데이터를 xls와 csv 형태로 저장하기
df = pd.DataFrame()
df['번호']=no2
df['제목']=pd.Series(title2)
df['저자']=pd.Series(writer2)
df['소속(발행)기관']=pd.Series(org2)

print(df)