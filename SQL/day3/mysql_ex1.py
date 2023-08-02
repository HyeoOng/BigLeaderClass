# riss.kr에서 빅데이터 관련 학위논문 제목 db에 저장

# 1. MySQL 관련 모듈 설치
## mysql-connector-python 설치(Terminal에서 pip install mysql-connector-python 입력)
import mysql.connector

# 2. 연결 설정
db = mysql.connector.connect(
    host = '127.0.0.1',  # loclhost 써도 무방 / 포트번호 3306이 기본이어서 따로 적지 않아도 됨(다르면 따로 설정해줘야함)
    user = 'root',
    password = 'mysql',
    database = 'riss_title'
)

## cursor(커서) 변수 선언 - db를 연결할 수 있는 기능 전달
cursor = db.cursor()
print('\n 연결 성공!')

# 3. 데이터 적재
import requests
from bs4 import BeautifulSoup

url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=bib_t&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=search&isFDetailSearch=N&sflag=1&searchQuery=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn='
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

## 데이터 추출하기.
titles = soup.find('div', class_='srchResultListW').find_all('p', 'title')

for idx, i in enumerate(titles, start=1):
    title = i.get_text()
    print(f'제목 : { title }')

    query  = "INSERT INTO riss_title.title (s_title) VALUES('{title}');"
    cursor.execute(query)
    db.commit()
    # db.config()
print('성공이요~')
# 4. MySQL 연결 종료
cursor.close()
db.close()